const Answer = require('../models/answersModel');
const multer = require('multer');
const path = require('path');

const storage = multer.diskStorage({
    destination: (req, file, cb) =>{
        cb(null, 'AnswerFiles')
    },
    filename: (req, file, cb) =>{
        const originalname = file.originalname.split('.').slice(0, -1).join('.');
        const timestamp = Date.now();
        const extension = path.extname(file.originalname);
        const newFilename = `${originalname}_${timestamp}${extension}`;
        cb(null, newFilename);
    }
});

exports.upload = multer({
    storage: storage,
    limits: { fieldSize: '25000000' },
    fileFilter: (req, file, cb) =>{
        const fileTypes = /docx|doc|zip/
        const mimeType = fileTypes.test(file.mimetype)
        const extname = fileTypes.test(path.extname(file.originalname))

        if (mimeType && extname){
            return cb(null, true)
        }

        cb('Not supported file format')
    }
}).single('answer_file_path');

exports.createNewAnswer = async (req, res, next) =>{
    try {
        let { user_id, exercise_id, grade } = req.body;
        let answer_file_path = req.file.path;

        const answer = new Answer(user_id, exercise_id, grade, answer_file_path);

        await answer.save();

        res.status(201).json({message:"Created new Answer"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getAllAnswers = async (req, res, next) =>{
    try {
        const [answers, _] = await Answer.findAll();

        res.status(200).json({count: answers.length, answers});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getAnswersByExId = async (req, res, next) =>{
    try {
        let exId = req.params.exId;

        const [answers, _] = await Answer.findAllByExId(exId);

        res.status(200).json({count: answers.length, answers});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.giveGrade = async (req, res, next) => {
    try {
        const answersToUpdate = req.body; // Array of answers with grades

        // Iterate over each answer
        for (const answerData of answersToUpdate) {
            const { id, grade } = answerData;

            // Update the grade for the answer with the given ID
            await Answer.updateGrade(id, grade);
        }

        res.status(200).json({ message:"Grades saved successfully"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}