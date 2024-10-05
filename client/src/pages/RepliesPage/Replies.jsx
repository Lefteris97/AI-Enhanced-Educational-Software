import DataTable from '../../components/DataTable'
import { repliesColumns } from '../../dtsource'
import './Replies.css'

const Replies = () =>{
    return (
        <div className="posts">
            <div className="info">
                <h1>Replies</h1>
            </div>
            <DataTable slug="replies" columns={repliesColumns}/>
        </div> 
    )
}

export default Replies