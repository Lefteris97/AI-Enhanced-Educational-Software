import { useContext, useState } from 'react';
import './Edit.css'
import axios from 'axios';
import AuthContext from '../../context/AuthProvider';

const EditUser = (props) =>{
    const { user } = props;
    const { auth } = useContext(AuthContext);
    
    // Check if user exists and has at least one item before accessing it
    if (!user || user.length === 0) {
        return <div>No user data available</div>;
    }

    const userDetails = user[0];

    const [editedUser, setEditedUser] = useState(userDetails);
    const [isEditing, setIsEditing] = useState(false);

    // Function to handle input changes and update editedUser state
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setEditedUser((prevUser) => ({
            ...prevUser,
            [name]: value,
        }));
    };

    // Function to handle update button click
    const handleUpdateClick = async () => {
        try {
            const response = await axios.put(
                `http://localhost:8000/users/${userDetails.id}`, 
                editedUser,
                {
                    headers: {
                        Authorization: `Bearer ${auth.accessToken}`
                    }
                }
            );

            console.log('User updated:', response.data);
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="itemPage">
            <div className="info">
                <div className="infoHeader">
                    <h1>{userDetails.fname}  {userDetails.lname}</h1>
                    <button onClick={handleUpdateClick}>Update</button>
                </div>
                <div className="details">
                    {Object.entries(userDetails).map(([key, value]) => (
                        <div className="item" key={key}>
                            {key === 'id' ? (
                                <>
                                    <span className="itemTitle">{key}:</span>
                                    <span className="itemValue">{userDetails[key]}</span>
                                </>
                            ) : (
                                <>
                                    <span className="itemTitle">{key}:</span>
                                    <input
                                        className="itemValue"
                                        type="text"
                                        name={key}
                                        value={isEditing ? editedUser[key] || "" : value} // Display edited value if available
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

export default EditUser;