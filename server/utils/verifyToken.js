const jwt = require('jsonwebtoken');
require('dotenv').config();

const verifyToken = (req, res, next) => {
    const authHeader = req.headers.authorization || req.headers.Authorization;
    if (!authHeader?.startsWith('Bearer ')) return res.sendStatus(401);

    const token = authHeader.split(' ')[1];

    jwt.verify(
        token,
        process.env.ACCESS_TOKEN_SECRET,
        (err, decoded) =>{

            if (err) {
                console.log('Token verification error:', err);
                return res.sendStatus(403); // Invalid token
            }

            req.user = decoded.UserInfo.email;
            req.role = decoded.UserInfo.role;
            req.user_id = decoded.UserInfo.user_id;
            next();
        }
    );
}

module.exports = verifyToken