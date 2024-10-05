import { useParams } from 'react-router-dom'
import './PostDetails.css'
import { useContext, useEffect, useState } from 'react';
import AuthContext from '../../context/AuthProvider';
import useFetch from '../../hooks/useFetch';
import axios from 'axios';

const PostDetails = () =>{
    const { post_id } = useParams();
    const { auth }= useContext(AuthContext);

    const { data: postData, loading: loadingPost, error: errorPost } = useFetch(`http://localhost:8000/posts/${post_id}`);
    const { data: repliesData, loading: loadingReplies, error: errorReplies, reFetch: refetchReplies } = useFetch(`http://localhost:8000/replies/of_post/${post_id}`);

    const [post, setPost] = useState(null);
    const [replies, setReplies] = useState([]);
    const [newReply, setNewReply] = useState('');

    useEffect(() => {
        if (postData && postData.post && Array.isArray(postData.post)){
            setPost(postData.post[0]);
        }
    }, [postData]);

    useEffect(() => {
        if (repliesData && repliesData.replies && Array.isArray(repliesData.replies)){
            setReplies(repliesData.replies);
        }
    }, [repliesData]);

    if (loadingPost || loadingReplies) {
        return <div>Loading data...</div>;
    }

    if (errorPost || errorReplies) {
        return <div>Error: {error.message}</div>;
    }

    const handleReplySubmit = async (e) =>{
        e.preventDefault();
        try {
            const response = await axios.post(
                'http://localhost:8000/replies',
                {
                    user_id: auth.user_id,
                    post_id: post_id,
                    content: newReply
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${auth.accessToken}`
                    }
                }
            );
            if (response.status === 201) {
                refetchReplies();
                setNewReply('');
            } else {
                console.log('Failed to create new reply');
            }
        } catch (error) {
            console.log('Error creating new reply:', error);
        }
        console.log('New Reply Submitted')
    };

    const handleNewReply = (e) =>{
        setNewReply(e.target.value);
    };

    return (
        <>
            {post && (
                <>
                <h1>{post.title}</h1>
                <h2 className='postAuthor'>Post by: {post.fname} {post.lname}</h2>
                <p className='postContent'>{post.post_content}</p>
                </>
            )}
            <h2>Replies ({replies.length}):</h2>
            {replies.length > 0 && (
                <>
                    <ul className='repliesList'>
                        {replies.map((reply) => (
                            <li key={reply.reply_id} className='replyItem'>
                                <h2>Reply by: {reply.fname} {reply.lname} ({reply.role})</h2>
                                <p>{reply.content}</p>
                            </li>
                        ))}
                    </ul>
                </>
            )}
            <div className="addReplyContainer">
                <h2>Add a reply:</h2>
                <form className='addReplyForm' onSubmit={handleReplySubmit}>
                    <textarea className='replyTextArea'
                        type="text"
                        value={newReply.content}
                        onChange={handleNewReply}
                        placeholder="Add a reply"
                        required
                    />
                    <button className='submitReplyButton' type="submit">Post Reply</button>
                </form>
            </div>
        </>
    )
}

export default PostDetails