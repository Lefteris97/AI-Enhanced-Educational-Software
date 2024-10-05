const Exercise = require('../models/exercisesModel')
const multer = require('multer')
const path = require('path')

const storage = multer.diskStorage({
    destination: (req, file, cb) =>{
        cb(null, 'Files')
    },
    filename: (req, file, cb) =>{
        // cb(null, Date.now() + path.extname(file.originalname))
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
}).single('file_path');

exports.createNewExercise = async (req, res, next) =>{
    try {
        let ex_name = req.body.ex_name;
        let file_path = req.file.path;

        console.log('ex_name:', ex_name);
        console.log('file_path:', file_path);

        const exercise = new Exercise(ex_name, file_path);

        await exercise.save();

        res.status(201).json({message:"Created new Exercise"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.getExerciseById = async (req, res, next) =>{
    try {
        let exId = req.params.id;
        let [ex, _] = await Exercise.findById(exId); // _ because we dont use the second value

        res.status(200).json({ex});
    } catch (error) {
        console.log(error);
        next(error); //send it to global error handler
    }
}

exports.getAllExercises = async (req, res, next) =>{
    try {
        const [exercises, _] = await Exercise.findAll();  

        res.status(200).json({count: exercises.length, exercises});
    } catch (error) {
        console.log(error);
        next(error);
    }
}

exports.updateExercise = async (req, res, next) =>{
    try {
        let extId = req.params.id;
        let ex_name = req.body.ex_name;

        // Check if req.file exists
        let file_path_updated = req.file ? req.file.path : req.body.file_path;

        console.log('UPDATED FILE PATH: ', file_path_updated);

        const [updatedEx, _] = await Exercise.updateById(extId, ex_name, file_path_updated);

        res.status(200).json({updatedEx});
    } catch (error) {
        console.log(error);
        next(error);
    }
}


exports.deleteExercise = async (req, res, next)=>{
    try {
        let exId = req.params.id;
        await Exercise.deleteById(exId);

        res.status(200).json({"message" : "Exercise has been deleted"});
    } catch (error) {
        console.log(error);
        next(error);
    }
}