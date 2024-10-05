const Post = require('../models/postsModel');

exports.createNewPost = async (req, res, next) =>{
    try {
        let {user_id, title, post_content} = req.body;

        const post = new Post(user_id, title, post_content);

        await post.save();

        res.status(201).json({message:"Created new Post"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getAllPosts = async (req, res, next) =>{
    try {
        const [posts, _] = await Post.findAll();

        res.status(200).json({count: posts.length, posts});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getPostById = async (req, res, next) =>{
    try {
        const postId = req.params.post_id;
        const [post, _] = await Post.findById(postId);

        res.status(200).json({post});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.deletePost = async (req, res, next)=>{
    try {
        let postId = req.params.post_id;
        await Post.deleteById(postId);

        res.status(200).json({"message" : "Post has been deleted"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}