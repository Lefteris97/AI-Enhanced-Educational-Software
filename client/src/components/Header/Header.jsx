import './Header.css'

const Header = () =>{

    const logout = () =>{
        console.log('Clicked Logout Button!');
        window.open("http://localhost:8000/auth/logout", "_self")
    };

    return (
        <div className="header">
            <div className='title'>Ez English</div>
            <button className='logoutBtn' onClick={logout}>Logout</button> 
        </div>
    )
}

export default Header