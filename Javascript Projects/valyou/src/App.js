import './App.css';
import NavBar from './AppComponents/AppBar';
import HomePage from './Pages/Home';
import MensPage from './Pages/Men';

function App() {
  const title = "Val(You)"

  return (
    <div className="App">
      <div className="content">
        <h1 className='title'>
          { title }
        </h1>
        <NavBar />
        <HomePage />
      </div>
    </div>
  );
}

export default App;
