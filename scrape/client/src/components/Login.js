import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import '../App.css';

const Login = (props) => {

    const {firstName,setFirstName,lastName,setLastName,email,setEmail,password,setPassword} = props
    const [confirmPassword,setConfirmPassword] = useState("")
    const [errors,setErrors] = useState([])
    const navigate = useNavigate()

    const registerHandler = (e) => {
        e.preventDefault()
        const user = {
            "first_name":firstName,
            "last_name":lastName,
            "email":email,
            "password":password,
            "confirm_password":confirmPassword
        }
        fetch("http://localhost:5000/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(user)
        }).then(response => response.json()
        ).then(data => {
            if(data["results"].length > 0){
                setErrors(data["results"])
                navigate("/login")
            }else{
                navigate("/home")
            }
        }).catch(() => {
            console.log("An error occured")
            navigate("/login")
        })
    }

    const loginHandler = (e) => {
        e.preventDefault()
        const user = {
            "email":email,
            "password":password
        }
        fetch("http://localhost:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(user)
        }).then(() => {
            console.log(user)
            console.log("user has logged in")
            // navigate("/home")
        }).catch(() => {
            console.log("An error occured")
            navigate("/login")
        })
    }

    return (
        <div className='loginContainer'>
            <div className='loginHeader'>
                <h1>Ray and Matt's App!</h1>
            </div>
            <div className='loginContent'>
                <form className='registerForm' onSubmit={registerHandler}>
                    <h2>Register</h2>
                    <div className='inputblocks'>
                        <label>First Name:</label><br/>
                        <input className='input' onChange={(e) => setFirstName(e.target.value)} type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Last Name:</label><br/>
                        <input className='input' onChange={(e) => setLastName(e.target.value)} type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Email:</label><br/>
                        <input className='input' onChange={(e) => setEmail(e.target.value)} type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Password:</label><br/>
                        <input className='input' onChange={(e) => setPassword(e.target.value)} type="password"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Confirm Password:</label><br/>
                        <input className='input' onChange={(e) => setConfirmPassword(e.target.value)} type="password"/>
                    </div>
                    <div>
                        <input className='registerButton' type="submit" value="Register"/>
                    </div>
                </form>
                <form className='loginForm' onSubmit={loginHandler}>
                    <h2>Login</h2>
                    <div className='inputblocks'>
                        <label>Email:</label><br/>
                        <input className='input' onChange={(e) => setEmail(e.target.value)} type="text"/>
                    </div>
                    <div className='inputblocks'>
                        <label>Password:</label><br/>
                        <input className='input' onChange={(e) => setPassword(e.target.value)} type="password"/>
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