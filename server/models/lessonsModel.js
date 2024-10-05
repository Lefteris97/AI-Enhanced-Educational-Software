const db = require('../database')

class Lesson{
    constructor(lesson_fields){
        this.title = lesson_fields.title;
        this.content = lesson_fields.content;
    }

    save(){
        let q = `
        INSERT INTO lessons(
            title,
            content
        )
        VALUES(
            '${this.title}',
            '${this.content}'
        )
        `;

        return db.execute(q);
    }

    static findAll(){
        let q = `SELECT * FROM lessons`;

        return db.execute(q);
    }

    static findById(id){
        let q = `SELECT * FROM lessons WHERE id = ?`;

        return db.execute(q, [id]);
    }

    static updateById(id, lesson_fields){
        let q = `
        UPDATE lessons
        SET title = ?,
            content = ?
        WHERE id = ?
        `;

        return db.execute(q, [lesson_fields.title, lesson_fields.content, id]);
    }

    static deleteById(id){
        let q = `DELETE FROM lessons WHERE id = ?`;

        return db.execute(q, [id]);
    }
}

module.exports = Lesson