import { useParams } from "react-router-dom"
import useFetch from "../../hooks/useFetch";
import EditExercise from "../../components/EditExercise/EditExercise";

const ExerciseDash = () =>{
    const { id } = useParams();

    const { data, loading, error } = useFetch(`http://localhost:8000/exercises/${id}`);
    
    if (loading) {
        return <div>Loading user data...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return(
        <div className="exercise">
            {data && <EditExercise {...data}/>}
        </div>
    )
}

export default ExerciseDash