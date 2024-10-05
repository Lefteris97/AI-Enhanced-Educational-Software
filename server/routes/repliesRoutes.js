const router = require('express').Router();
const repliesController = require('../controllers/repliesController');
const verifyToken = require('../utils/verifyToken');
const verifyRoles = require('../utils/verifyRoles');

//CREATE
router.post("/", verifyToken, verifyRoles('admin', 'teacher', 'student'), repliesController.createNewReply);

//GET ALL
router.get("/", verifyToken, verifyRoles('admin', 'teacher', 'student'), repliesController.getAllReplies);

//GET REPLIES BY POST ID
router.get("/of_post/:post_id", verifyToken, verifyRoles('admin', 'teacher', 'student'), repliesController.getRepliesByPostId);

//DELETE
router.delete("/:reply_id", verifyToken, verifyRoles('admin'), repliesController.deleteReply);

module.exports = router