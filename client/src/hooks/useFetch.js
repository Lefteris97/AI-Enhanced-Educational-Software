import { useEffect, useState, useContext } from 'react';
import axios from 'axios';
import AuthContext from '../context/AuthProvider';

const useFetch = (url) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);

    // Access the auth context
    const { auth } = useContext(AuthContext);

    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                // Include Authorization header if accessToken is available
                const options = auth.accessToken ? { 
                    headers: { 'Authorization': `Bearer ${auth.accessToken}` } 
                } : {};

                const res = await axios.get(url, options);
                setData(res.data);
            } catch (error) {
                setError(true);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [url, auth.accessToken]); // Depend on url and accessToken changes

    // Similar adjustment for reFetch to include auth if necessary
    const reFetch = async () => {
        setLoading(true);
        try {
            const options = auth.accessToken ? { 
                headers: { 'Authorization': `Bearer ${auth.accessToken}` } 
            } : {};

            const res = await axios.get(url, options);
            setData(res.data);
        } catch (error) {
            setError(true);
        } finally {
            setLoading(false);
        }
    };

    return { data, loading, error, reFetch };
};

export default useFetch;