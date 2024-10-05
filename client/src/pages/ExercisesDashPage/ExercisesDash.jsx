import './ExercisesDash.css'
import { useState } from 'react'
import { useParams } from 'react-router-dom'
import { AiOutlineReload } from "react-icons/ai";
import DataTable from '../../components/DataTable';
import { exerciseColumns } from '../../dtsource'
import { exerciseInputs } from '../../formSource'
import AddExercise from '../../components/AddExercise/AddExercise';

const ExercisesDash = () =>{
    const [open, setOpen] = useState(false);
    const [reloadComponent, setReloadComponentd] = useState(false);

    const handleReloadComponent = () =>{
        setReloadComponentd(prevState => !prevState);
    };

    return (
        <div className="exercises">
            <div className="info">
                <h1>Exercises</h1>
                <button onClick={() => setOpen(true)}>Add New Exercise</button>
                <AiOutlineReload size={22} onClick={handleReloadComponent}/>
            </div>
            <DataTable key={reloadComponent ? 'reload' : 'normal'} slug="exercises" columns={exerciseColumns}/>
            {open && <AddExercise slug="exercise" inputs={exerciseInputs} setOpen={setOpen}/>}
        </div>
    )
}

export default ExercisesDash