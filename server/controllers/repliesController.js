const Reply = require('../models/repliesModel');

exports.createNewReply = async (req, res, next) =>{
    try {
        let {user_id, post_id, content} = req.body;

        const reply = new Reply(user_id, post_id, content);

        await reply.save();

        res.status(201).json({message:"Created new Reply"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getAllReplies = async (req, res, next) =>{
    try {
        const [replies, _] = await Reply.findAll();

        res.status(200).json({count: replies.length, replies});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getRepliesByPostId = async (req, res, next) =>{
    try {
        const postId = req.params.post_id;
        const [replies, _] = await Reply.findRepliesByPostId(postId);

        res.status(200).json({count: replies.length, replies});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.deleteReply = async (req, res, next) =>{
    try {
        let replyId = req.params.reply_id;
        await Reply.deleteById(replyId);

        res.status(200).json({"message" : "Reply has been deleted"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}