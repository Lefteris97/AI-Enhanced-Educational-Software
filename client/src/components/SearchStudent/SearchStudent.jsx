import { useState } from 'react'
import './SearchStudent.css'
import { GrFormSearch } from "react-icons/gr";
import axios from 'axios';

const SearchStudent = ({onStudentSelect}) =>{ 
    const [searchId, setSearchId] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [data, setData] = useState(null);

    const handleInputChange = (e) =>{
        setSearchId(e.target.value);
    };

    const handleSearch = async () => {
        if (searchId) {
            setLoading(true);
            setError(null);
            setData(null);

            try {
                const response = await axios.get(`http://127.0.0.1:8000/student/${searchId}`);
                setData(response.data);
                onStudentSelect(response.data); // Call the parent callback with the data
            } catch (err) {
                setError('Student not found or an error occurred.');
                onStudentSelect(null); // Reset the student state
            } finally {
                setLoading(false);
            }
        }
    };

    return (
        <>
            <div className='searchBar'>
                <strong>Enter Student ID: </strong>   
                <input 
                    type='number'
                    value={searchId}
                    onChange={handleInputChange}
                    style={{width: '60px'}}
                />
                <GrFormSearch className='searchIcon' size={32} onClick={handleSearch} />
            </div>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </>
    )
};

export default SearchStudent