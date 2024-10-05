import { useEffect, useState } from 'react';
import useFetch from '../../hooks/useFetch';
import './Theory.css'
import { Link } from 'react-router-dom';

const Theory = () =>{
    const { data, loading, error } = useFetch('http://localhost:8000/lessons');

    const [lessons, setLessons] = useState([]);

    useEffect(() => {
        if (data && data.lessons && Array.isArray(data.lessons)) {
            setLessons(data.lessons);
        }
    }, [data]);

    // Check if data is loading or if there's an error
    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <>
            <h1 className='lessonsHeader'>Lessons</h1>
            <ul className='lessonsList'>
                { lessons.map(lesson => (
                    <Link to={`/lesson/${lesson.id}/${lesson.title}`} key={lesson.id} className='lessonItems'>
                        <li key={lesson.id}>
                            <h2>{lesson.title}</h2>
                        </li>
                    </Link>
                ))}

            </ul>
        </>
    )
}

export default Theory