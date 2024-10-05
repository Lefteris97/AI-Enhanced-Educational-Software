const router = require('express').Router()
const authController = require('../controllers/authController')
require('dotenv').config({path:"../.env"})

//create new user
router.post("/register", authController.register);

router.post("/login", authController.login);

router.get("/login/succeeded", (req, res) =>{
    if(req.user){
        res.status(200).json({
            success: true,
            message: "successful authentication",
            user: req.user,
            cookies: req.cookies
        });
    }   
});

router.get("/login/failed", (req, res) =>{
    res.status(401).json({
        success: false,
        message: "error during authentication",
    });
});

router.get("/logout", (req, res)=>{
    // req.logout();
    res.clearCookie('jwt', {httpOnly: true});
    res.redirect("http://localhost:5555/");
})

module.exports = router