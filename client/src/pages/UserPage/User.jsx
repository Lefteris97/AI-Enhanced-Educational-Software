import './User.css'
import { useParams } from 'react-router-dom';
import useFetch from '../../hooks/useFetch';
import EditUser from '../../components/EditUser';

const User = () =>{ 

    const { id } = useParams();

    const { data, loading, error } = useFetch(`http://localhost:8000/users/${id}`);

    if (loading) {
        return <div>Loading user data...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <div className="user">
            {data && <EditUser {...data}/>}
        </div>
    )
}

export default User