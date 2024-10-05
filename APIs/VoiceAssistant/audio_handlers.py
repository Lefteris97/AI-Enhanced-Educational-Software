from fastapi import HTTPException, UploadFile, BackgroundTasks
from gtts import gTTS
import os
import speech_recognition as sr
import tempfile
import subprocess
import datetime
from fastapi.responses import FileResponse
from pydub import AudioSegment
from io import BytesIO
from responses_handler import load_responses, find_response

NOTES_FOLDER = "saved_notes"
NOTES_COMMANDS = ["make a note", "make note", "remember this", "write that down", "write this down", "create note", "create a note", "keep note"]

# Load responses once during the app start
responses = load_responses()

async def text_to_audio_converter(text: str, background_tasks: BackgroundTasks):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    temp_filename = temp_file.name
    try:
        # Generate speech from text and save it to the temporary file
        tts = gTTS(text=text, lang='en')
        tts.save(temp_filename)
        
        # Add the task to delete the file after response is sent
        background_tasks.add_task(os.remove, temp_filename)
        
        # Return the file response
        return FileResponse(temp_filename, media_type="audio/mpeg", filename="output.mp3")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating audio: {str(e)}")


async def audio_to_text_converter(file: UploadFile):
    recognizer = sr.Recognizer()
    try:
        audio_data = await file.read()
        audio_file = BytesIO(audio_data)

        audio_segment = AudioSegment.from_file(audio_file)
        wav_file = BytesIO()
        audio_segment.export(wav_file, format="wav")
        wav_file.seek(0)

        with sr.AudioFile(wav_file) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio).lower()  # Convert to lower case for comparison

        # Check for note-taking command
        for command in NOTES_COMMANDS:
            if command in text:
                # Remove the command phrase from the text
                note_text = text.replace(command, '').strip()
                await write_down_audio(note_text)  # Handle note creation
                return {"command": "create note", "text": note_text}
        
        # If no command is recognized
        response_text = find_response(text, responses)
        
        return {"rec_text": text, "res_text": response_text}

    except sr.UnknownValueError:
        raise HTTPException(status_code=400, detail="Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        raise HTTPException(status_code=503, detail=f"Could not request results from Google Speech Recognition service; {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing audio: {str(e)}")


async def write_down_audio(text):
    # Check if the notes folder exists, and create it if not
    if not os.path.exists(NOTES_FOLDER):
        os.makedirs(NOTES_FOLDER)

    # Generate a filename based on the current date and time
    date = datetime.datetime.now()
    file_name = f"{date.strftime('%Y-%m-%d_%H-%M-%S')}_note.txt"
    file_path = os.path.join(NOTES_FOLDER, file_name)  # Full path to save the note

    try:
        # Write the text to the note file
        with open(file_path, "w") as f:
            print('Saved at ', file_path)
            f.write(text)

        # Open the note file in Notepad (for Windows)
        subprocess.Popen(["notepad.exe", file_path])

    except Exception as e:
        print(f"Error creating note: {e}")