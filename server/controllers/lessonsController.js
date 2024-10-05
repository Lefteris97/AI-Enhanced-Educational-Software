const Lesson = require('../models/lessonsModel')

exports.createNewLesson = async (req, res, next) =>{
    try {
        let lesson_fields = req.body;

        const lesson = new Lesson(lesson_fields);

        await lesson.save();

        res.status(201).json({message:"Created new Lesson"});

    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getLessonById = async (req, res, next) =>{
    try {
        let lessonId = req.params.id;
        let [lesson, _] = await Lesson.findById(lessonId);

        res.status(200).json({lesson});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getAllLessons = async (req, res, next) =>{
    try {
        const [lessons, _] = await Lesson.findAll();

        res.status(200).json({count: lessons.length, lessons});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.updateLesson = async (req, res, next) =>{
    try {
        let lessonId = req.params.id;
        let lesson_fields = req.body;

        const [updatedLesson, _] = await Lesson.updateById(lessonId, lesson_fields);

        res.status(200).json({updatedLesson});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.deleteLesson = async (req, res, next) =>{
    try {
        let lessonId = req.params.id;

        await Lesson.deleteById(lessonId);

        res.status(200).json({"message" : "Lesson has been deleted"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}