import React, {useState, useRef} from 'react'
import { useNavigate } from 'react-router-dom';
import '../App.css';
import '../static/CSS/login_registration_profile.css';
import bcrypt from 'bcryptjs'

const Registration = (props) => {

    const {firstName,setFirstName,lastName,setLastName,email,setEmail,password,setPassword} = props
    const [confirmPassword,setConfirmPassword] = useState("")
    const [phoneNumber,setPhoneNumber] = useState("000-000-0000")
    const [errors,setErrors] = useState([])
    const navigate = useNavigate()

    const registerHandler = (e) => {
        e.preventDefault()
        if(password.length < 8){
            var hashedPassword = "Password must be at least 8 characters."
        }else{
            var hashedPassword = bcrypt.hashSync(password, 10)
        }
        if(hashedPassword == "Password must be at least 8 characters."){
            if(password == confirmPassword){
                var hashedPasswordCheck = true
            }else{
                var hashedPasswordCheck = false
            }
        }else{
            var hashedPasswordCheck = bcrypt.compareSync(confirmPassword, hashedPassword)
        }
        // if(PASSWORD_REGEX.test(password)){
        //     setPasswordRegEx(true)
        // }else{
        //     setPasswordRegEx(false)
        // }
        const user = {
            "first_name":firstName,
            "last_name":lastName,
            "email":email,
            "password":hashedPassword,
            "confirm_password":hashedPasswordCheck,
            "phone_number":phoneNumber
        }
        fetch("http://localhost:5000/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(user)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data.results)
            if(data.results.length > 0){
                setErrors(data.results)
            }else{
                navigate("/home")
            }
        }).catch(() => {
            console.log("An error occured")
            navigate("/registration")
        })
    }

    return (
        <section>
            <div className='container-register'>
                <div className='header'>
                    <h1>Sign Up</h1>
                </div>
                <form className='registerForm' onSubmit={registerHandler}>
                    <div className='errors'>
                        {
                            errors?
                            errors.map((item,index) => (
                                <div key={index}>
                                    <p>{item}</p>
                                </div>
                            )):
                            ""
                        }
                    </div>
                    <div className='inputblocks'>
                        <label>First Name</label>
                        <div className='inputblocks-bottom'>
                            <svg style={{height: 24, width: 24, marginRight: 12, stroke: "#757575"}} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M17.982 18.725A7.488 7.488 0 0012 15.75a7.488 7.488 0 00-5.982 2.975m11.963 0a9 9 0 10-11.963 0m11.963 0A8.966 8.966 0 0112 21a8.966 8.966 0 01-5.982-2.275M15 9.75a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                            <input className='input' onChange={(e) => setFirstName(e.target.value)} type="text" placeholder='Enter your first name'/>
                        </div>
                    </div>
                    <div className='inputblocks'>
                        <label>Last Name</label>
                        <div className='inputblocks-bottom'>
                            <svg style={{height: 24, width: 24, marginRight: 12, stroke: "#757575"}} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
                            </svg>
                            <input className='input' onChange={(e) => setLastName(e.target.value)} type="text" placeholder='Enter your last name'/>
                        </div>
                    </div>
                    <div className='inputblocks'>
                        <label>Email</label>
                        <div className='inputblocks-bottom'>
                            <svg style={{height: 24, width: 24, marginRight: 12, stroke: "#757575"}} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 13.5h3.86a2.25 2.25 0 012.012 1.244l.256.512a2.25 2.25 0 002.013 1.244h3.218a2.25 2.25 0 002.013-1.244l.256-.512a2.25 2.25 0 012.013-1.244h3.859m-19.5.338V18a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18v-4.162c0-.224-.034-.447-.1-.661L19.24 5.338a2.25 2.25 0 00-2.15-1.588H6.911a2.25 2.25 0 00-2.15 1.588L2.35 13.177a2.25 2.25 0 00-.1.661z" />
                            </svg>
                            <input className='input' onChange={(e) => setEmail(e.target.value)} type="text" placeholder='Enter your email'/>
                        </div>
                    </div>
                    <div className='inputblocks'>
                        <label>Password</label>
                        <div className='inputblocks-bottom'>
                            <svg style={{height: 24, width: 24, marginRight: 12, stroke: "#757575"}} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
                            </svg>
                            <input className='input' onChange={(e) => setPassword(e.target.value)} type="password" placeholder='Enter your password'/>
                        </div>
                    </div>
                    <div className='inputblocks'>
                        <label>Confirm Password</label>
                        <div className='inputblocks-bottom'>
                            <svg style={{height: 24, width: 24, marginRight: 12, stroke: "#757575"}} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <input className='input' onChange={(e) => setConfirmPassword(e.target.value)} type="password" placeholder='Confirm your password'/>
                        </div>
                    </div>
                    <div className='inputblocks'>
                        <label>Phone Number (Optional)</label>
                        <div className='inputblocks-bottom'>
                            <svg style={{height: 24, width: 24, marginRight: 12, stroke: "#757575"}} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6">
                                <path strokeLinecap="round" strokeLinejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3" />
                            </svg>
                            <input className='input' onChange={(e) => setPhoneNumber(e.target.value)} type="text" placeholder='Enter your phone number'/>
                        </div>
                    </div>
                    <div>
                        <input className='button' type="submit" value="REGISTER"/>
                    </div>
                </form>
                <div className='login-link'>
                    <p>Already Have An Account?</p>
                    <a href="/login">LOGIN &rarr;</a>
                </div>
            </div>
        </section>
    )
}

export default Registration