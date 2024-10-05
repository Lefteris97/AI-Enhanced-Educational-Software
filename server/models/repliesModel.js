const db = require('../database');

class Reply{
    constructor(user_id, post_id, content){
        this.user_id = user_id;
        this.post_id = post_id;
        this.content = content;
    }

    save(){
        let q = `
        INSERT INTO replies(
            user_id,
            post_id,
            content
        )
        VALUES(
            '${this.user_id}',
            '${this.post_id}',
            '${this.content}'
        )
        `;

        return db.execute(q);
    }

    static findAll(){
        let q = `
            SELECT reply_id, id, content, fname, lname, role
            FROM replies 
            JOIN posts ON replies.post_id = posts.post_id
            JOIN users ON replies.user_id = users.id
        `;

        return db.execute(q);
    }

    static findRepliesByPostId(postId){
        let q = `
            SELECT reply_id, id, content, fname, lname, role
            FROM replies 
            JOIN posts ON replies.post_id = posts.post_id
            JOIN users ON replies.user_id = users.id
            WHERE posts.post_id = ?;
        `;

        return db.execute(q, [postId]);
    }

    static deleteById(id){
        let q = `DELETE FROM replies WHERE reply_id = ?`;

        return db.execute(q, [id]);
    }
}

module.exports = Reply