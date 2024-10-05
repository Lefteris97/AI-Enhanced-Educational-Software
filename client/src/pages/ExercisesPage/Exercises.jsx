import { useEffect, useState, useContext } from 'react';
import useFetch from '../../hooks/useFetch';
import './Exercises.css';
import { BiSolidSave } from "react-icons/bi";
import { ImFolderUpload } from "react-icons/im";
import axios from 'axios';
import AuthContext from '../../context/AuthProvider';

const Exercises = () => {
    const { auth } = useContext(AuthContext);

    // Use the custom hook to fetch exercises and answers
    const { data: exData, loading: loadingEx, error: errorEx, reFetch: reFetchEx } = useFetch('http://localhost:8000/exercises');
    const { data: anData, loading: loadingAn, error: errorAn, reFetch: reFetchAn } = useFetch('http://localhost:8000/answers');

    const [exercises, setExercises] = useState([]);
    const [answers, setAnswers] = useState([]);
    const [essayFile, setEssayFile] = useState(null);
    const [feedback, setFeedback] = useState(null);

    useEffect(() => {
        if (exData && exData.exercises && Array.isArray(exData.exercises)) {
            setExercises(exData.exercises);
        }
    }, [exData]);

    useEffect(() => {
        if (anData && anData.answers && Array.isArray(anData.answers)) {
            const userAnswers = anData.answers.filter(answer => answer.user_id === auth.user_id);
            setAnswers(userAnswers);
        }
    }, [anData, auth]);

    const handleFileChange = (exerciseId, event) => {
        const file = event.target.files[0];
        console.log(`File selected for exercise ${exerciseId}:`, file);
    };

    const handleSubmitClick = async (exerciseId, userId) => {
        const fileInput = document.getElementById(`file_${exerciseId}`);
        const file = fileInput.files[0];

        if (!file) {
            console.error('No file selected.');
            return;
        }

        const formData = new FormData();
        formData.append('user_id', userId);
        formData.append('exercise_id', exerciseId);
        formData.append('answer_file_path', file);

        try {
            await axios.post(
                'http://localhost:8000/answers',
                formData,
                {
                    headers: {
                        Authorization: `Bearer ${auth.accessToken}`,
                        'Content-Type': 'multipart/form-data'
                    }
                }
            );

            console.log('Answer uploaded successfully.');
            // Refetch data to update the page
            reFetchEx();
            reFetchAn();
        } catch (error) {
            console.log('Error uploading answer:', error.message);
        }
    };

    if (loadingEx || loadingAn) {
        return <div>Loading exercises data...</div>;
    }

    if (errorEx || errorAn) {
        return <div>Error: {errorEx?.message || errorAn?.message}</div>;
    }

    const handleEssayChange = (event) => {
        const file = event.target.files[0];
        setEssayFile(file);
    };

    const handleEssaySubmit = async () => {
        if (!essayFile) {
            console.error('No file selected.');
            return;
        }

        const formData = new FormData();
        formData.append('file', essayFile);

        try {
            const response = await axios.post(
                'http://127.0.0.1:8000/submit_essay',
                formData,
                {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
            );

            setFeedback(response.data.feedback);
        } catch (error) {
            console.error('Error submitting essay:', error.message);
        }
    };

    return (
        <>
            <h1 className='exHeader'>Exercises</h1>
            <ul className='exercisesList'>
                {exercises.map(exercise => {
                    const answer = answers.find(answer => answer.exercise_id === exercise.id);
                    const grade = answer !== undefined && answer !== null ? answer.grade : ' ';

                    return (
                        <li key={exercise.id} className='exerciseItem'>
                            <div className='exerciseName'>
                                <h2>{exercise.ex_name}</h2>
                            </div>
                            <div className='exerciseFile'>
                                <a href={`http://localhost:8000/${exercise.file_path}`} download>
                                    <BiSolidSave size={26} />
                                </a>
                            </div>
                            <div className='uploadAnswer'>
                                <strong htmlFor={`file_${exercise.id}`} className='answerLabel'>
                                    Upload Answer: <ImFolderUpload size={22} />
                                </strong>
                                <input
                                    type="file"
                                    id={`file_${exercise.id}`}
                                    onChange={(e) => handleFileChange(exercise.id, e)}
                                    disabled={!!answer} // Disable file input if an answer exists
                                />
                                <button 
                                    onClick={() => handleSubmitClick(exercise.id, auth.user_id)} 
                                    disabled={!!answer} // Disable submit button if an answer exists
                                >
                                    Submit
                                </button>
                            </div>
                            <div className='exerciseGrade'>
                                <h2>{grade}/10</h2>
                            </div>
                        </li>
                    );
                })}
            </ul>
            <h1 className='esHeader'>Essays</h1>
            <div className='esInput'>
                <strong className='uploadEssayLabel'>
                    Upload Essay: <ImFolderUpload size={22} />
                </strong>
                <input
                    type="file"
                    accept=".docx"
                    onChange={handleEssayChange}
                />
                <button onClick={handleEssaySubmit}>Submit</button>
            </div>
            {feedback && (
                <div className='feedback'>
                    <h2>Feedback</h2>
                    <ul>
                        {feedback.map((item, index) => (
                            <li key={index} className='feedbackItem'>
                                <strong>Message:</strong> {item.message}<br />
                                <strong>Category:</strong> {item.ruleIssueType}<br />
                                <strong>Sentence:</strong> {item.sentence}<br />
                                <strong>Replacements:</strong> {Array.isArray(item.replacements) && item.replacements.length > 0 ? item.replacements.join(', ') : 'No replacements'}<br />
                                <strong>Offset:</strong> {item.offset}
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </>
    );
}

export default Exercises;
