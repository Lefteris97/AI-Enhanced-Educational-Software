const router = require('express').Router()
const exerciseController = require('../controllers/exerciseController')
const verifyToken = require('../utils/verifyToken');
const verifyRoles = require('../utils/verifyRoles');

//CREATE
router.post("/", verifyToken, verifyRoles('admin', 'teacher'), exerciseController.upload, exerciseController.createNewExercise);

//GET
router.get("/:id", verifyToken, verifyRoles('admin', 'teacher', 'student'), exerciseController.getExerciseById);

//GET ALL
router.get("/", verifyToken, verifyRoles('admin', 'teacher', 'student'), exerciseController.getAllExercises);

//UPDATE
router.put("/:id", verifyToken, verifyRoles('admin', 'teacher'), exerciseController.upload, exerciseController.updateExercise);

//DELETE
router.delete("/:id", verifyToken, verifyRoles('admin', 'teacher'), exerciseController.deleteExercise);

module.exports = router