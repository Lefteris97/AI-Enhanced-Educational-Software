import './TheoryDash.css'
import { lessonColumns } from '../../dtsource'
import { useState } from 'react'
import AddLesson from '../../components/AddLesson'
import DataTable from '../../components/DataTable'
import { lessonInputs } from '../../formSource'
import { AiOutlineReload } from "react-icons/ai";

const TheoryDash = () =>{

    const [open, setOpen] = useState(false);
    const [reloadComponent, setReloadComponent] = useState(false);

    const handleReloadComponent = () => {
        setReloadComponent(prevState => !prevState);
    };

    return (
        <div className='lessons'>
            <div className="info">
                <h1>Lessons</h1>
                <button onClick={() => setOpen(true)}>Add New Lesson</button>
                <AiOutlineReload size={22} onClick={handleReloadComponent}/>
            </div>
            <DataTable key={reloadComponent ? 'reload' : 'normal'} slug="lessons" columns={lessonColumns}/>
            {open && <AddLesson slug="lesson" inputs={lessonInputs} setOpen={setOpen}/>}
        </div>
    )
}

export default TheoryDash