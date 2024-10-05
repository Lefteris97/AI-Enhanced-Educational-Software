import './EzBot.css';
import { useRef, useState } from 'react';
import axios from 'axios';
import { FaMicrophoneAlt, FaMicrophoneAltSlash } from 'react-icons/fa';

const EzBot = () => {
    const mediaRecorderRef = useRef(null);
    const [recording, setRecording] = useState(false);
    const audioChunksRef = useRef([]);
    const [conversation, setConversation] = useState([]);

    // Function to play the text to speech response from the backend
    const handleSpeak = async (textToSpeak) => {
        try {
            const response = await axios.post(
                'http://127.0.0.1:8001/speak',
                { text: textToSpeak },
                { responseType: 'blob' }
            );

            const url = window.URL.createObjectURL(new Blob([response.data]));
            const audio = new Audio(url);
            audio.play();

            // console.log('EzBot is saying: ', textToSpeak);

            // Update conversation with EzBot's response
            setConversation(prev => [...prev, { sender: 'bot', text: textToSpeak }]);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    // Function to handle audio capture from the microphone
    const handleAudioCapture = async () => {
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                const mediaRecorder = new MediaRecorder(stream);
                mediaRecorderRef.current = mediaRecorder;
                audioChunksRef.current = [];

                mediaRecorder.ondataavailable = (e) => {
                    audioChunksRef.current.push(e.data);
                };

                mediaRecorder.onstop = async () => {
                    if (audioChunksRef.current.length > 0) {
                        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/wav' });
                        try {
                            const formData = new FormData();
                            formData.append('file', audioBlob, 'audio.wav');

                            const response = await axios.post('http://127.0.0.1:8001/recognize', formData, {
                                headers: { 'Content-Type': 'multipart/form-data' }
                            });

                            const recognizedText = response.data.rec_text;
                            const responseText = response.data.res_text;

                            // Update conversation with the user's recognized speech
                            setConversation(prev => [...prev, { sender: 'user', text: recognizedText }]);

                            // Handle note creation based on backend response
                            if (response.data.command === 'create note') {
                                await handleSpeak("I've made a note on that.");
                            } else {
                                await handleSpeak(responseText);
                            }

                        } catch (error) {
                            console.error("Error sending audio to backend:", error);
                        }
                    } else {
                        console.error("No audio data captured.");
                    }
                };

                setRecording(true);
                mediaRecorder.start();
            } catch (error) {
                console.error("Error accessing microphone:", error);
            }
        }
    };

    const toggleRecording = () => {
        if (recording) {
            if (mediaRecorderRef.current) {
                mediaRecorderRef.current.stop();
            }
        } else {
            handleAudioCapture();
        }
        setRecording(!recording);
    };

    return (
        <div className='EzBotContainer'>
            <h1 className='ezbotHeader'>EzBot</h1>
            <div className="conversationScreen">
                {conversation.map((msg, index) => (
                    <div key={index} className={`message ${msg.sender}`}>
                        <strong>{msg.sender === 'user' ? '' : 'EzBot:'}</strong> {msg.text}
                        {/* {msg.text} */}
                    </div>
                ))}
            </div>

            <button
                className={`recordBtn ${recording ? 'recording' : 'not_recording'}`}
                onClick={toggleRecording}
            >
                {recording ? (
                    <FaMicrophoneAlt size={23} />
                ) : (
                    <FaMicrophoneAltSlash size={23} />
                )}
            </button>
        </div>
    );
};

export default EzBot;