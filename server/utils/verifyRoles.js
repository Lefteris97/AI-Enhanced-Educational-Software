const verifyRoles = (...allowedRoles) =>{
    return (req, res, next) =>{
        if (!req?.role) return res.sendStatus(401);

        const result = allowedRoles.includes(req.role);

        if(!result) return res.sendStatus(401);

        next();
    }
}

module.exports = verifyRoles