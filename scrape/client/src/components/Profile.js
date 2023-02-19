import React, {useState} from 'react'
import { Link, useParams } from 'react-router-dom'
import '../App.css';

const Profile = (props) => {

    const {firstName,setFirstName,lastName,setLastName,email,setEmail,password,setPassword} = props
    const [confirmPassword,setConfirmPassword] = useState("")
    const {id} = useParams()

    // use id from useParams and useEffect to get database info and set props to those values.


    return (
        <div className='profileContainer'>
            <div className='profileNavbar'>
                <Link to={'/home'}>Home</Link>
                <Link to={'/dashboard'}>My Dashboard</Link>
                <Link to={'/'}>Logout</Link>
            </div>
            <div className='profileContent'>
                <h3>Update Profile</h3>
                <form action="" className='updateForm'>
                    <div className='inputblocks'>
                        <label>First Name:</label><br/>
                        <input className='input' type="text" onChange={(e) => setFirstName(e.target.value)} value={firstName}/>
                    </div>
                    <div className='inputblocks'>
                        <label>Last Name:</label><br/>
                        <input className='input' type="text" onChange={(e) => setLastName(e.target.value)} value={lastName}/>
                    </div>
                    <div className='inputblocks'>
                        <label>Email:</label><br/>
                        <input className='input' type="text" onChange={(e) => setEmail(e.target.value)} value={email}/>
                    </div>
                    <div className='inputblocks'>
                        <label>Password:</label><br/>
                        <input className='input' type="password" onChange={(e) => setPassword(e.target.value)}/>
                    </div>
                    <div className='inputblocks'>
                        <label>Confirm New Password:</label><br/>
                        <input className='input' type="password" onChange={(e) => setConfirmPassword(e.target.value)}/>
                    </div>
                    <div>
                        <input className='registerButton' type="submit" value="Update"/>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Profile