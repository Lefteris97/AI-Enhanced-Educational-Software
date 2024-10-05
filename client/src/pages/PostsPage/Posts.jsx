import DataTable from '../../components/DataTable'
import { postsColumns } from '../../dtsource'
import './Posts.css'

const Posts = () => {
    return (
        <div className="posts">
            <div className="info">
                <h1>Posts</h1>
            </div>
            <DataTable slug="posts" columns={postsColumns}/>
        </div> 
    )
}

export default Posts