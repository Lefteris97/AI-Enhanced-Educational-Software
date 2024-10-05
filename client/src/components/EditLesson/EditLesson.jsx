import '../EditUser/Edit.css'
import { useContext, useState } from 'react';
import axios from 'axios';
import AuthContext from '../../context/AuthProvider';

const EditLesson = (props) =>{
    const { lesson } = props;
    const { auth } = useContext(AuthContext);
    
    // Check if user exists and has at least one item before accessing it
    if (!lesson || lesson.length === 0) {
        return <div>No lesson data available</div>;
    }

    const lessonDetails = lesson[0];

    const [editedLesson, setEditedLesson] = useState(lessonDetails);
    const [isEditing, setIsEditing] = useState(false);

    // Function to handle input changes and update editedUser state
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setEditedLesson((prevLesson) => ({
            ...prevLesson,
            [name]: value,
        }));
    };

    // Function to handle update button click
    const handleUpdateClick = async () => {
        try {
            const response = await axios.put(
                `http://localhost:8000/lessons/${lessonDetails.id}`, 
                editedLesson,
                {
                    headers: {
                        Authorization: `Bearer ${auth.accessToken}`
                    }
                }
            );

            console.log('Lesson updated:', response.data);
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="itemPage">
            <div className="info">
                <div className="infoHeader">
                    <h1>{lessonDetails.title}</h1>
                    <button onClick={handleUpdateClick}>Update</button>
                </div>
                <div className="details">
                    {Object.entries(lessonDetails).map(([key, value]) => (
                        <div className="item" key={key}>
                            {key === 'id'  ? (
                                <>
                                    <span className="itemTitle">{key}:</span>
                                    <span className="itemValue">{lessonDetails[key]}</span>
                                </>
                            ) : (
                                <>
                                    <span className="itemTitle">{key}:</span>
                                    <input
                                        className="itemValue"
                                        type="text"
                                        name={key}
                                        value={isEditing ? editedLesson[key] || "" : value} // Display edited value if available
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

export default EditLesson;