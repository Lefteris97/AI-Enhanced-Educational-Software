import './Home.css'
import homeImage from '../../assets/english_home.jpg'

const Home = () =>{

    return (
        <div className='home'>
            <h1>Welcome to Ez English!</h1>
            <h2>Learn English Online</h2>
            <img src={homeImage} alt="Home Page Image" className='homeImage'/>
        </div>
    )
}

export default Home