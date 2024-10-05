import './LessonDash.css'
import { useParams } from 'react-router-dom';
import useFetch from '../../hooks/useFetch';
import EditLesson from '../../components/EditLesson'

const LessonDash = () =>{

    const { id } = useParams();
    
    const { data, loading, error } = useFetch(`http://localhost:8000/lessons/${id}`);

    if (loading) {
        return <div>Loading user data...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <div className='lesson'>
            {data && <EditLesson {...data}/>}
        </div>
    )
}

export default LessonDash