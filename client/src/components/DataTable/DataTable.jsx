import { Link, useLocation } from 'react-router-dom';
import './DataTable.css'
import { DataGrid, GridToolbar } from '@mui/x-data-grid';
import { BiEdit } from "react-icons/bi";
import { AiOutlineDelete } from "react-icons/ai";
import useFetch from '../../hooks/useFetch'
import { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import AuthContext from '../../context/AuthProvider';

const DataTable = (props) =>{
    const location = useLocation();
    const path = location.pathname.split("/")[2];
    const [list, setList] = useState([]);
    const { auth } = useContext(AuthContext);

    const {data, loading, error} = useFetch(`http://localhost:8000/${path}`);

    useEffect(() =>{
        if (data && data[path]){
            setList(data[path])
        }
    }, [data]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    if (list.length === 0) {
        return <div>No data available</div>;
    }

    const uniqueIdentifier = Object.keys(list[0])[0];
    
    const handleDelete = async (id) =>{
        try {
            await axios.delete(`http://localhost:8000/${path}/${id}`, 
                {
                    headers: {
                        Authorization: `Bearer ${auth.accessToken}`
                    }
                }
            );
            
            setList((prevList) => prevList.filter((item) => item[uniqueIdentifier] !== id));
        } catch (error) {
            console.log(error);
        }
    };

    const actionColumn = {
        field: "action",
        headerName: "Action",
        sortable: false,
        width: 80,
        renderCell: (params) =>{
            const shouldRender = props.slug !== 'posts' && props.slug !== 'replies';

            return (
                <div className="action">
                    {shouldRender && (
                        <Link to={`/dash/${props.slug}/${params.row[uniqueIdentifier]}`}>
                            <BiEdit size={22} color='#4d79ff' />
                        </Link>
                    )}
                    <div className="delete" onClick={()=>handleDelete(params.row[uniqueIdentifier])}>
                        <AiOutlineDelete size={22} color='#cc0000'/>
                    </div>
                </div>
            )
        }
    }
    
    return (
        <div className="dataTable">
            <DataGrid 
                className='dataGrid'
                rows={list}
                columns={[...props.columns, actionColumn]}
                initialState={{
                pagination: {
                    paginationModel: {
                    pageSize: 10,
                    },
                },
                }}
                slots={{toolbar: GridToolbar}}
                slotProps={{
                    toolbar:{
                        showQuickFilter: true,
                        quickFilterProps: {debounceMs: 500}
                    }
                }}
                pageSizeOptions={[10]}
                checkboxSelection
                disableRowSelectionOnClick
                disableColumnFilter
                disableDensitySelector
                disableColumnSelector
                getRowId={(row) => row[uniqueIdentifier]}
            />
        </div>
    )
}

export default DataTable