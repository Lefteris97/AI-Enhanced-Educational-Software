import { useContext, useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import useFetch from '../../hooks/useFetch';
import './Forum.css';
import AuthContext from '../../context/AuthProvider';
import axios from 'axios';

const Forum = () => {
    const { data, loading, error, reFetch } = useFetch('http://localhost:8000/posts');
    const { auth } = useContext(AuthContext);

    const [posts, setPosts] = useState([]);
    const [newPost, setNewPost] = useState({ title: '', content: '' });

    useEffect(() => {
        if (data && data.posts && Array.isArray(data.posts)) {
            setPosts(data.posts);
        }
    }, [data]);

    if (loading) {
        return <div>Loading posts data...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    const handleFormSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post(
                'http://localhost:8000/posts',
                {
                    user_id: auth.user_id, 
                    title: newPost.title,
                    post_content: newPost.content
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${auth.accessToken}`
                    }
                }
            );

            if (response.status === 201) {
                reFetch();
                setNewPost({ title: '', content: '' });
            } else {
                console.log('Failed to create new post');
            }
        } catch (error) {
            console.log('Error creating new post:', error);
        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewPost((prevPost) => ({ ...prevPost, [name]: value }));
    };

    return (
        <>
            <h1 className="forumHeader">Community Hub</h1>
            <div className="newPostContainer">
                <h2 className="newPostHeader">Make a New Post!</h2>
                <form className="newPostForm" onSubmit={handleFormSubmit}>
                    <input className='postTitleInput'
                        type="text"
                        name="title"
                        value={newPost.title}
                        onChange={handleInputChange}
                        placeholder="Post Title"
                        required
                    />
                    <textarea className='textAreaPost'
                        name="content"
                        value={newPost.content}
                        onChange={handleInputChange}
                        placeholder="Post Content"
                        required
                    />
                    <button className='submitPostButton' type="submit">Create New Post</button>
                </form>
            </div>
            
            <ul className="postsList">
                {posts.map((post) => (
                    <li key={post.post_id} className="postItem">
                        <div className="postTitle">
                            <h2 className='postTitle'>
                                <Link to={{ pathname: `/posts/${post.post_id}`, state: { post } }}>
                                    {post.title}
                                </Link>
                            </h2>
                            <h3 className='postDetails'>
                                By: {post.fname} {post.lname}
                            </h3>
                        </div>
                    </li>
                ))}
            </ul>
        </>
    );
};

export default Forum;
