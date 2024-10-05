const db = require('../database')


class Exercise{
    constructor(ex_name, file_path){
        this.ex_name = ex_name;
        this.file_path = file_path;
    }

    save(){
        let filePathValue = `'${this.file_path.replace(/\\/g, '/')}'`;

        let q = `
        INSERT INTO exercises(
            ex_name,
            file_path
        )
        VALUES(
            '${this.ex_name}',
            ${filePathValue}
        )
        `;

        return db.execute(q);
    }

    static findAll(){
        let q = `SELECT * FROM exercises`;

        return db.execute(q);
    }

    static findById(id){
        let q = `SELECT * FROM exercises WHERE id = ?`;

        return db.execute(q, [id]);
    }

    static updateById(id, ex_name, file_path){

        let filePathValue = `'${file_path.replace(/\\/g, '/')}'`;
        console.log('WHAT : ', filePathValue);

        let q = `
            UPDATE exercises
            SET ex_name = ?,
                file_path = ?
            WHERE id = ?
        `;

        return db.execute(q, [ex_name, filePathValue, id]);
    }

    static deleteById(id){
        let q = `DELETE FROM exercises WHERE id = ?`;

        return db.execute(q, [id]);
    }
}

module.exports = Exercise