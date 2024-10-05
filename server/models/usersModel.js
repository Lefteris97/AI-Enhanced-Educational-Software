const db = require('../database')

class User{
    constructor(fname, lname, email, password, role){
        this.fname = fname;
        this.lname = lname;
        this.email = email;
        this.password = password;
        this.role = role;
    }

    save(){

        let q = `
        INSERT INTO users(
            fname,
            lname,
            email,
            password,
            role
        )
        VALUES(
            '${this.fname}',
            '${this.lname}',
            '${this.email}',
            '${this.password}',
            '${this.role}'
        )
        `;

        return db.execute(q);

    }

    //for login
    static getUserByEmail(email){

        let q = `SELECT * FROM users WHERE email = ?`;
        
        return db.execute(q, [email]);
    }

    static findAll(){
        let q = `SELECT * FROM users`;

        return db.execute(q);
    }

    static findById(id){
        let q = `SELECT * FROM users WHERE id = ?`;

        return db.execute(q, [id]);
    }

    static updateById(id, fname, lname, email, password, role){
        let q = `
            UPDATE users
            SET fname = ?,
                lname = ?,
                email = ?,
                password = ?,
                role = ?
            WHERE id = ?
        `;

        return db.execute(q, [fname, lname, email, password, role, id]);
    }

    static deleteById(id){
        let q = `DELETE FROM users WHERE id = ?`;

        return db.execute(q, [id]);
    }

}

module.exports = User