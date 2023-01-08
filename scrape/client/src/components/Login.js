import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import '../App.css';

const Login = (props) => {

    const {firstName,setFirstName,lastName,setLastName} = props
    const [email,setEmail] = useState("")
    const [password,setPassword] = useState("")
    const navigate = useNavigate()

    const registerHandler = (e) => {
        e.preventDefault()
    }

    const loginHandler = (e) => {
        e.preventDefault()
    }

    return (
        <div>
            <div className='loginHeader'>
                <h1>Ray and Matt's App!</h1>
            </div>
            <div className='loginContent'>
                <form action="" className='registerForm' onSubmit={registerHandler}>
                    <h2>Register</h2>
                    <div className='inputblocks'>
                        <label>First Name:</label><br/>
                        <input className='input' type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Last Name:</label><br/>
                        <input className='input' type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Email:</label><br/>
                        <input className='input' type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Password:</label><br/>
                        <input className='input' type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Confirm Password:</label><br/>
                        <input className='input' type="text"/>
                    </div>
                    <div>
                        <input className='registerButton' type="submit" value="Register"/>
                    </div>
                </form>
                <form action="" className='loginForm' onSubmit={loginHandler}>
                    <h2>Login</h2>
                    <div className='inputblocks'>
                        <label>Email:</label><br/>
                        <input className='input' type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Password:</label><br/>
                        <input className='input' type="text"/>
                    </div>
                    <div>
                        <input className='loginButton' type="submit" value="Login"/>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Login