import './Users.css'
import { userColumns } from '../../dtsource'
import { useState } from 'react'
import AddUser from '../../components/AddUser'
import DataTable from '../../components/DataTable'
import { userInputs } from '../../formSource'
import { AiOutlineReload } from "react-icons/ai";

const Users = () =>{

    const [open, setOpen] = useState(false);
    const [reloadComponent, setReloadComponent] = useState(false);

    const handleReloadComponent = () => {
        setReloadComponent(prevState => !prevState);
    };

    return (
        <div className='users'>
            <div className="info">
                <h1>Users</h1>
                <button onClick={() => setOpen(true)}>Add New User</button>
                <AiOutlineReload size={22} onClick={handleReloadComponent}/>
            </div>
            <DataTable key={reloadComponent ? 'reload' : 'normal'} slug="users" columns={userColumns}/>
            {open && <AddUser slug="user" inputs={userInputs} setOpen={setOpen}/>}
        </div>
    )
}

export default Users