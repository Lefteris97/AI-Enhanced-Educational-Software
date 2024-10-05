import { Link, useParams } from 'react-router-dom'
import useFetch from '../../hooks/useFetch'
import './Lesson.css'

const Lesson = () =>{
    const { id } = useParams();
    const { data, loading, error } = useFetch(`http://localhost:8000/lessons/${id}`);

    if (loading) {
        return <div>Loading lesson data...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    // Check if event data exists
    if (!data || !data.lesson || data.lesson.length === 0) {
        return <div>No lesson data found</div>;
    }

    // Access the lesson data inside the event array
    const lesson = data.lesson[0];

    return (
        <div className='lessonDetails'>
            {lesson ? (
                <>  
                    <div className="lessonTitle">
                        <h2>{lesson.title}</h2>
                    </div>
                    <div className="lessonContent">
                        <p>{lesson.content}</p> 
                    </div>
                </>
            ) : (
                <div>Lesson not found</div>
            )}
            <div className="backContainer">
                <Link to='/theory' className='backLink'>Back to Lessons</Link>
            </div>
        </div>
    )
}

export default Lesson
