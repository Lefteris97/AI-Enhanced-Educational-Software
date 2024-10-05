import './Menu.css'
import { Link } from 'react-router-dom'
import { AiFillHome, AiOutlineTeam } from "react-icons/ai";
import { BiBook, BiSolidPencil } from "react-icons/bi";
import { GrChatOption } from "react-icons/gr";
import { BsFillReplyAllFill } from "react-icons/bs";
import { FaFilePen } from "react-icons/fa6";
import { GiProgression } from "react-icons/gi";
import { LiaRobotSolid } from "react-icons/lia";

const Menu = ({role}) =>{

    return (
        <div className="menu">
            <div className="menuItem">
                <span className="title">MENU</span>
                <Link to={'/'} className='listItem'>
                    <AiFillHome size={21}/>
                    <span className="listItemTitle">Home</span>
                </Link>
                <Link to={'/theory'} className='listItem'>
                    <BiBook size={21}/>
                    <span className="listItemTitle">Theory</span>
                </Link>
                <Link to={'/exercises'} className='listItem'>
                    <BiSolidPencil size={21}/>
                    <span className="listItemTitle">Exercises</span>
                </Link>
                <Link to={'/ezbot'} className='listItem'>
                    <LiaRobotSolid size={24}/>
                    <span className="listItemTitle">EzBot</span>
                </Link>
                <Link to={'/forum'} className='listItem'>
                    <GrChatOption size={21}/>
                    <span className="listItemTitle">Forum</span>
                </Link>
                {(role === 'admin' || role === 'teacher') && (
                    <>
                        <span className="title">DASHBOARD</span>
                        
                        {role === 'admin' && (
                        <>
                            <Link to={'/dash/users'} className="listItem">
                                <AiOutlineTeam size={21}/>
                                <span className="listItemTitle">Users</span>
                            </Link>
                        </>
                        )}
                        <Link to={'/dash/lessons'} className="listItem">
                            <BiBook size={21}/>
                            <span className="listItemTitle">Theory</span>
                        </Link>
                        <Link to={'/dash/exercises'} className="listItem">
                            <BiSolidPencil size={21}/>
                            <span className="listItemTitle">Exercises</span>
                        </Link>
                        {role === 'admin' && (
                        <>
                            <Link to={'/dash/posts'} className="listItem">
                                <FaFilePen size={21}/>
                                <span className="listItemTitle">Posts</span>
                            </Link>
                            <Link to={'/dash/replies'} className="listItem">
                                <BsFillReplyAllFill size={21}/>
                                <span className="listItemTitle">Replies</span>
                            </Link>
                        </>
                        )}
                        {role === 'teacher' && (
                        <>
                            <Link to={'/dash/student_progress'} className="listItem">
                                <GiProgression size={21}/>
                                <span className="listItemTitle">Progression</span>
                            </Link>
                        </>
                        )}
                    </>
                )}
            </div>
        </div>
    )
}

export default Menu