const db = require('../database');

class Answer{
    constructor(user_id, exercise_id, grade, answer_file_path){
        this.user_id = user_id;
        this.exercise_id = exercise_id;
        this.answer_file_path = answer_file_path;
        this.grade = grade;
    }

    save(){
        let answerPathValue = `'${this.answer_file_path.replace(/\\/g, '/')}'`;

        let gradeValue = this.grade !== undefined && this.grade !== null ? `'${this.grade}'` : 'DEFAULT';

        let q = `
        INSERT INTO answers(
            user_id,
            exercise_id,
            answer_file_path,
            grade
        )
        VALUES(
            '${this.user_id}',
            '${this.exercise_id}',
            ${answerPathValue},
            ${gradeValue}
        )
        `;

        return db.execute(q);
    }

    static findAll(){
        let q = `SELECT * FROM answers`;

        return db.execute(q);
    }

    static findAllByExId(exId){
        let q = `
            SELECT * FROM answers
            WHERE exercise_id = ?
        `;

        return db.execute(q, [exId]);
    }

    static updateGrade(answerId, newGrade){
        let q = `
            UPDATE answers
            SET grade = ?
            WHERE id = ?
        `;

        return db.execute(q, [newGrade, answerId]);
    }
}

module.exports = Answer