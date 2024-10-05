const express = require('express')
const cors = require('cors')
const cookieSession = require('cookie-session')
const cookieParser = require('cookie-parser')
const authRoutes = require('./routes/authRoutes')
const usersRoutes = require('./routes/usersRoutes')
const lessonsRoutes = require('./routes/lessonsRoutes')
const exercisesRoutes = require('./routes/exercisesRoutes')
const answersRoutes = require('./routes/answersRoutes')
const postsRoutes = require('./routes/postsRoutes')
const repliesRoutes = require('./routes/repliesRoutes')

const app = express()

app.use(cookieSession({
    name:"session",
    keys:["mpsp2308"],
    maxAge: 24 * 60 * 60 * 1000   // 1 day
}));

app.use(cors(
    {
        origin: "http://localhost:5555",
        methods:"GET, POST, PUT, DELETE",
        credentials:true
    }
));

app.use(cookieParser());
app.use(express.json()); //to send json

app.use("/auth", authRoutes);
app.use("/users", usersRoutes);
app.use("/lessons", lessonsRoutes);
app.use("/exercises", exercisesRoutes);
app.use("/answers", answersRoutes);
app.use("/posts", postsRoutes);
app.use("/replies", repliesRoutes);

app.use("/Files", express.static("./Files"));
app.use("/AnswerFiles", express.static("./AnswerFiles"));

//global error handling middleware
app.use((err, req, res, next) => {
    const errorStatus = err.status || 500
    const errorMessage = err.message || "An error has occured!"
    return res.status(errorStatus).json({
        success: false,
        status: errorStatus,
        message: errorMessage
    });
})

app.listen(8000, () => {console.log("Server started on port 8000")});