import './App.css';
import {BrowserRouter, Routes, Router, Route, Navigate} from 'react-router-dom';
import { useState, useEffect } from 'react';
import Login from './components/Login';
import Home from './components/Home';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [currentTime, setCurrentTime] = useState(1)
  const [firstName, setFirstName] = useState("")
  const [lastName, setLastName] = useState("")

  useEffect(() => {
    fetch("http://127.0.0.1:5000/time")
    .then(res => res.json())
    .then(data => {
      setCurrentTime(data.time)
      console.log(data)
    })
  },[])

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Navigate to ='/login'/>}/>
          <Route path='/login' element={<Login firstName={firstName} setFirstName={setFirstName} lastName={lastName} setLastName={setLastName}/>}/>
          <Route path='/home' element={<Home />}/>
          
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;