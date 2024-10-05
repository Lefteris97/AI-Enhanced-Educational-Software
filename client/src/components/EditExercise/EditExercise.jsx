import { useContext, useState } from 'react';
import '../EditUser/Edit.css'
import axios from 'axios';
import AuthContext from '../../context/AuthProvider';
import { ImFolderUpload } from "react-icons/im";

const EditExercise = (props) =>{

    const { ex: exercise } = props;
    const { auth } = useContext(AuthContext);
    
    // Check if exercise exists and has at least one item before accessing it
    if (!exercise || exercise.length === 0) {
        return <div>No exercise data available</div>;
    }

    const exerciseDetails = exercise[0];

    const [editedExercise, setEditedExercise] = useState(exerciseDetails);
    const [isEditing, setIsEditing] = useState(false);

    const [filePath, setFilePath] = useState(exerciseDetails.file_path);

    // // Function to handle input changes and update editedExercise state
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setEditedExercise((prevExercise) => ({
            ...prevExercise,
            [name]: value,
        }));
    };

    // // Function to handle update button click
    const handleUpdateClick = async () => {
        const formData = new FormData();

        // Append new file if it is selected
        if (filePath instanceof File) {
            console.log('new file selected for update');
            formData.append('file_path', filePath);
        } else {
            console.log('using old file path');
            formData.append('file_path', exerciseDetails.file_path);
        }

        console.log('file path: ', filePath);

        // Append other form data
        Object.entries(editedExercise).forEach(([key, value]) => {
            formData.append(key, value);
        });

        try {   
            const response = await axios.put(
                `http://localhost:8000/exercises/${exerciseDetails.id}`, 
                formData,
                {
                    headers: {
                        Authorization: `Bearer ${auth.accessToken}`,
                        'Content-Type': 'multipart/form-data'
                    }
                }
            );
            
            console.log('Exercise updated:', response.data);
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="itemPage">
            <div className="info">
                <div className="infoHeader">
                    <h1>{exerciseDetails.ex_name}</h1>
                    <button onClick={handleUpdateClick}>Update</button>
                </div> 
                <div className="fileUpload">
                    <label htmlFor="file" className='fileLabel'>
                        Exercise File: <ImFolderUpload size={22}/>
                    </label>
                    <input
                        type="file"
                        id="file_path"
                        onChange={(e) => setFilePath(e.target.files[0])}
                    />
                    <div className="fileContainer">
                        <span>Current File: </span>
                        <a href={`http://localhost:8000/${exerciseDetails.file_path}`} download>
                            {exerciseDetails.file_path.split('/').pop()}
                        </a>
                    </div>
                </div>
                <div className="details">
                    {Object.entries(exerciseDetails)
                        .filter(([key, value]) => !['file_path'].includes(key))
                        .map(([key, value]) => (
                            <div className="item" key={key}>
                                {key === 'id' ? (
                                    <>
                                        <span className="itemTitle">{key}:</span>
                                        <span className="itemValue">{exerciseDetails[key]}</span>
                                    </>
                                ) : (
                                    <>
                                        <span className="itemTitle">{key}:</span>
                                        <input
                                            className="itemValue"
                                            type="text"
                                            name={key}
                                            value={isEditing ? editedExercise[key] || "" : value}
                                            onChange={handleInputChange}
                                            onFocus={() => setIsEditing(true)}
                                            onBlur={() => setIsEditing(false)}
                                        />
                                    </>
                                )}
                            </div>
                    ))}
                </div>
            </div>
        </div>
    );
}

export default EditExercise;