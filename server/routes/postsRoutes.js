const router = require('express').Router();
const postsController = require('../controllers/postsController');
const verifyToken = require('../utils/verifyToken');
const verifyRoles = require('../utils/verifyRoles');

//CREATE
router.post("/", verifyToken, verifyRoles('admin', 'teacher', 'student'), postsController.createNewPost);

//GET ALL 
router.get("/", verifyToken, verifyRoles('admin', 'teacher', 'student'), postsController.getAllPosts);

//GET
router.get("/:post_id", verifyToken, verifyRoles('admin', 'teacher', 'student'), postsController.getPostById);

//DELETE
router.delete("/:post_id", verifyToken, verifyRoles('admin'), postsController.deletePost);

module.exports = router