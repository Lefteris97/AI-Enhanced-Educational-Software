import { useContext, useState } from 'react';
import '../AddUser/Add.css'
import { AiOutlineCloseCircle } from "react-icons/ai";
import { ImFolderUpload } from "react-icons/im";
import axios from 'axios';
import AuthContext from '../../context/AuthProvider';

const AddExercise = (props) =>{

    const [filePath, setFilePath] = useState('');
    const [info, setInfo] = useState({});
    const { auth } = useContext(AuthContext);

    const handleChange = (e) =>{
        setInfo(prev => ({...prev, [e.target.id]: e.target.value}));
    }

    const handleSubmit = async (e) =>{
        e.preventDefault();

        const formData = new FormData();

        formData.append('file_path', filePath);

        // Append other form data
        Object.keys(info).forEach(key => {
            formData.append(key, info[key]);
        });

        //add new item
        try {
            await axios.post(
                "http://localhost:8000/exercises",
                formData,
                {
                    headers: {
                        Authorization: `Bearer ${auth.accessToken}`,
                        'Content-Type': 'multipart/form-data'
                    }
                }
            );
            
            props.setOpen(false); 
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <div className="add">
            <div className="modal">
                <span className="close" onClick={() => props.setOpen(false)}><AiOutlineCloseCircle size={22}/></span>
                <h1>Add new {props.slug}</h1>
                <form onSubmit={handleSubmit}>
                    <div className="uploadFile">
                        <div className="fileUpload">
                                <label htmlFor="file">
                                    Exercise File: <ImFolderUpload size={22} className='uploadIcon'/>
                                </label>
                                <input
                                    type="file"
                                    id="file_path"
                                    onChange={(e) => setFilePath(e.target.files[0])}
                                />
                        </div>
                    </div>
                    {props.inputs.map(input => {
                            return (
                                <div className="item" key={input.id}>
                                    <label>{input.label}</label>
                                    <input onChange={handleChange} type={input.type} placeholder={input.placeholder} id={input.id}/>
                                </div>
                            );
                        })
                    }
                    <button>Save</button>
                </form>
            </div>
        </div>
    )
}

export default AddExercise