import './App.css';
import {BrowserRouter, Routes, Router, Route, Navigate} from 'react-router-dom';
import { useState, useEffect } from 'react';
import Login from './components/Login';
import Profile from './components/Profile';
import Home from './components/Home';
import Dashboard from './components/Dashboard';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  const [currentTime, setCurrentTime] = useState(1)
  const [firstName, setFirstName] = useState("")
  const [lastName, setLastName] = useState("")
  const [email,setEmail] = useState("")
  const [password,setPassword] = useState("")
  const [topSearches, setTopSearches] = useState([])
  const [watchList, setWatchList] = useState([])

  // useEffect(() => {
  //   fetch("http://127.0.0.1:5000/time")
  //   .then(res => res.json())
  //   .then(data => {
  //     setCurrentTime(data.time)
  //     console.log(data)
  //   })
  // },[])

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Navigate to ='/login'/>}/>
          <Route path='/login' element={<Login firstName={firstName} setFirstName={setFirstName} lastName={lastName} setLastName={setLastName} email={email} setEmail={setEmail} password={password} setPassword={setPassword}/>}/>
          <Route path='/home' element={<Home firstName={firstName} setFirstName={setFirstName} lastName={lastName} setLastName={setLastName} email={email} setEmail={setEmail} password={password} setPassword={setPassword} topSearches={topSearches} setTopSearches={setTopSearches} watchList={watchList} setWatchList={setWatchList}/>}/>
          <Route path='/profile' element={<Profile firstName={firstName} setFirstName={setFirstName} lastName={lastName} setLastName={setLastName} email={email} setEmail={setEmail} password={password} setPassword={setPassword}/>}/>
          <Route path='/dashboard' element={<Dashboard />}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;