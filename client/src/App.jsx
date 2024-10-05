import './App.css';
import { Navigate, Route, Routes } from "react-router-dom";
import useAuth from './hooks/useAuth';
import Header from './components/Header';
import Menu from './components/Menu';
import Home from './pages/HomePage';
import Login from './components/Login';
import Theory from './pages/TheoryPage';
import Exercises from './pages/ExercisesPage';
import Users from './pages/UsersPage';
import TheoryDash from './pages/TheoryDashPage';
import ExercisesDash from './pages/ExercisesDashPage';
import User from './pages/UserPage';
import LessonDash from './pages/LessonDashPage';
import Lesson from './pages/LessonPage';
import ExerciseDash from './pages/ExerciseDashPage';
import Answers from './pages/AnswersPage';
import Forum from './pages/ForumPage';
import PostDetails from './pages/PostDetailsPage';
import Posts from './pages/PostsPage';
import Replies from './pages/RepliesPage';
import NoAccess from './components/NoAccess';
import StudentProgress from './pages/StudentProgress';
import EzBot from './pages/EzBotPage';

const App = () =>{

  const { auth } = useAuth();

  const isLoggedIn = !!auth.accessToken;

  const Protected = ({children}) => {

    if(!isLoggedIn){
      return <Navigate to="/login"/>
    }

    return children;
  };

  const NoStudents = ({children}) =>{

    if(!isLoggedIn){
      return <Navigate to="/login"/>
    }

    if(auth.role !== 'admin' && auth.role !== 'teacher'){
      return <NoAccess/>
    }

    return children;
  };

  const OnlyTeachers = ({children}) =>{

    if(!isLoggedIn){
      return <Navigate to="/login"/>
    }

    if(auth.role !== 'teacher'){
      return <NoAccess/>
    }

    return children;
  };

  const FullSecure = ({children}) =>{

    if(!isLoggedIn){
      return <Navigate to="/login"/>
    }

    if(auth.role !== 'admin'){
      return <NoAccess/>
    }

    return children;
  };

  const Layout = ({children}) =>{
    return(
      <div className="main">
        <Header/>
        <div className="container">
          <div className="menuContainer">
            <Menu role={auth.role}/>
          </div>
          <div className="contentContainer">
            {children}
          </div>
        </div>
      </div>
    )
  };

  return (
    <>
      <Routes>
        <Route
          path="/"
          element={<Layout><Protected><Home/></Protected></Layout>}
        />
        <Route
          path="/login"
          element={<Login/>}
        />
        <Route
          path="/theory"
          element={<Layout><Protected><Theory/></Protected></Layout>}
        />
        <Route
          path="/exercises"
          element={<Layout><Protected><Exercises/></Protected></Layout>}
        />
        <Route
          path="/ezbot"
          element={<Layout><Protected><EzBot/></Protected></Layout>}
        />
        <Route
          path="/forum"
          element={<Layout><Protected><Forum/></Protected></Layout>}
        />
        <Route
          path="/posts/:post_id"
          element={<Layout><Protected><PostDetails/></Protected></Layout>}
        />
        <Route
          path="/dash/users"
          element={<Layout><FullSecure><Users/></FullSecure></Layout>}
        />
        <Route
          path="/dash/lessons"
          element={<Layout><NoStudents><TheoryDash/></NoStudents></Layout>}
        />
        <Route
          path="/dash/exercises"
          element={<Layout><NoStudents><ExercisesDash/></NoStudents></Layout>}
        />
        <Route
          path="/dash/users/:id"
          element={<Layout><FullSecure><User/></FullSecure></Layout>}
        />
        <Route
          path="/dash/lessons/:id"
          element={<Layout><NoStudents><LessonDash/></NoStudents></Layout>}
        />
        <Route
          path="/dash/exercises/:id"
          element={<Layout><NoStudents><ExerciseDash/></NoStudents></Layout>}
        />
        <Route
          path="/dash/posts"
          element={<Layout><FullSecure><Posts/></FullSecure></Layout>}
        />
        <Route
          path="/dash/replies"
          element={<Layout><FullSecure><Replies/></FullSecure></Layout>}
        />
        <Route
          path="/lesson/:id/:title"
          element={<Layout><Protected><Lesson/></Protected></Layout>}
        />
        <Route
          path="/dash/answers/for_ex/:exerciseId"
          element={<Layout><OnlyTeachers><Answers/></OnlyTeachers></Layout>}
        />
        <Route
          path='/dash/student_progress'
          element={<Layout><OnlyTeachers><StudentProgress/></OnlyTeachers></Layout>}
        />
      </Routes>
    </>
  )
}

export default App