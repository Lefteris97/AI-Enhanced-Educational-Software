const router = require('express').Router();
const userController = require('../controllers/usersController');
const verifyToken = require('../utils/verifyToken');
const verifyRoles = require('../utils/verifyRoles');

//GET
router.get("/:id", verifyToken, verifyRoles('admin', 'teacher', 'student'), userController.getUserById);

//GET ALL
router.get("/", verifyToken, verifyRoles('admin', 'teacher'), userController.getAllUsers);

//UPDATE
router.put("/:id", verifyToken, verifyRoles('admin'), userController.updateUser);

//DELETE
router.delete("/:id", verifyToken, verifyRoles('admin'), userController.deleteUser);

module.exports = router