import { useContext, useState } from 'react';
import '../AddUser/Add.css'
import { AiOutlineCloseCircle } from "react-icons/ai";
import axios from 'axios';
import AuthContext from '../../context/AuthProvider';

const AddLesson = (props) =>{
    const { auth } = useContext(AuthContext);

    const [info, setInfo] = useState({});

    const handleChange = (e) =>{
        setInfo(prev => ({...prev, [e.target.id]: e.target.value}));
    }

    const handleSubmit = async (e) =>{
        e.preventDefault();

        //add new item
        try {
            const newLesson = {
                ...info
            }

            await axios.post("http://localhost:8000/lessons", 
                        newLesson,
                        {
                            headers: {
                                Authorization: `Bearer ${auth.accessToken}`
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

export default AddLesson