const router = require('express').Router();
const answersController = require('../controllers/answersController');
const verifyToken = require('../utils/verifyToken');
const verifyRoles = require('../utils/verifyRoles');

//CREATE
router.post("/", verifyToken, verifyRoles('admin', 'teacher', 'student'), answersController.upload, answersController.createNewAnswer);

//GET
// router.get("/:", ;

//GET ALL
router.get("/", verifyToken, verifyRoles('admin', 'teacher', 'student'), answersController.getAllAnswers);

//GET ANSWERS BY EXERCISE ID
router.get("/of/:exId", verifyToken, verifyRoles('admin', 'teacher', 'student'), answersController.getAnswersByExId);

//UPDATE GRADES - PUT GRADES
router.put("/grade_answers", verifyToken, verifyRoles('teacher'), answersController.giveGrade);
    
module.exports = router