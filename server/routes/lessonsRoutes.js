const router = require('express').Router()
const lessonController = require('../controllers/lessonsController')
const verifyToken = require('../utils/verifyToken');
const verifyRoles = require('../utils/verifyRoles');

//CREATE
router.post("/", verifyToken, verifyRoles('admin', 'teacher'), lessonController.createNewLesson);

//GET
router.get("/:id", verifyToken, verifyRoles('admin', 'teacher', 'student'), lessonController.getLessonById);

//GET ALL
router.get("/", verifyToken, verifyRoles('admin', 'teacher', 'student'), lessonController.getAllLessons);

//UPDATE
router.put("/:id", verifyToken, verifyRoles('admin', 'teacher'), lessonController.updateLesson);

//DELETE
router.delete("/:id", verifyToken, verifyRoles('admin', 'teacher'), lessonController.deleteLesson);

module.exports = router