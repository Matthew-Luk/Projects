
import {BrowserRouter, Routes, Router, Route, Navigate} from 'react-router-dom';
import { useState, useEffect } from 'react';
import Login from './components/Login';
import Registration from './components/Registration';
import Profile from './components/Profile';
import Home from './components/Home';
import Dashboard from './components/Dashboard';

function App() {
  const [firstName, setFirstName] = useState("")
  const [lastName, setLastName] = useState("")
  const [email,setEmail] = useState("")
  const [password,setPassword] = useState("")
  const [topSearches, setTopSearches] = useState([])
  const [watchList, setWatchList] = useState([])

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Navigate to ='/login'/>}/>
          <Route path='/login' element={<Login email={email} setEmail={setEmail} password={password} setPassword={setPassword}/>}/>
          <Route path='/registration' element={<Registration firstName={firstName} setFirstName={setFirstName} lastName={lastName} setLastName={setLastName} email={email} setEmail={setEmail} password={password} setPassword={setPassword}/>}/>
          <Route path='/home' element={<Home firstName={firstName} setFirstName={setFirstName} lastName={lastName} setLastName={setLastName} email={email} setEmail={setEmail} password={password} setPassword={setPassword} topSearches={topSearches} setTopSearches={setTopSearches} watchList={watchList} setWatchList={setWatchList}/>}/>
          <Route path='/profile' element={<Profile firstName={firstName} setFirstName={setFirstName} lastName={lastName} setLastName={setLastName} email={email} setEmail={setEmail} password={password} setPassword={setPassword}/>}/>
          <Route path='/dashboard' element={<Dashboard />}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;