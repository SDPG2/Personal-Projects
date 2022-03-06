import logo from'./Instagram_icon.png'

const NavBar = () => {
    return (  
        <nav className="navbar">
            <div className="links">
                <a href="/">Home</a>
                <a href="/Men">Men</a>
                <a href="/Women">Women</a>
                <a href="/Contact">Contact</a>
                <a href="https://www.instagram.com/">
                    <img src={logo} width = "30" height = "30"/>
                </a>
            </div>
        </nav>
    );
}
 
export default NavBar;