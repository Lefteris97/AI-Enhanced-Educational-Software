const db = require('../database');

class Post{
    constructor(user_id, title, post_content){
        this.user_id = user_id;
        this.title = title;
        this.post_content = post_content;
    }

    save(){
        let q = `
        INSERT INTO posts(
            user_id,
            title,
            post_content
        )
        VALUES(
            '${this.user_id}',
            '${this.title}',
            '${this.post_content}'
        )
        `;

        return db.execute(q);
    }

    static findAll(){
        let q = `
            SELECT post_id, user_id, title, post_content, fname, lname
            FROM posts INNER JOIN users
            ON posts.user_id = users.id;
        `;

        return db.execute(q);
    }

    static findById(postId){
        let q = `
            SELECT post_id, user_id, title, post_content, fname, lname
            FROM posts INNER JOIN users
            ON posts.user_id = users.id
            WHERE posts.post_id = ?;
        `;

        return db.execute(q, [postId]);
    }

    static deleteById(id){
        let q = `DELETE FROM posts WHERE post_id = ?`;

        return db.execute(q, [id]);
    }
}

module.exports = Post