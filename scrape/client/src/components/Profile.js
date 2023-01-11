import React from 'react'
import { Link } from 'react-router-dom'
import '../App.css';

const Profile = () => {

    const updateHandler = (e) => {
        e.preventDefault()
    }

    return (
        <div className='profileContainer'>
            <div className='profileNavbar'>
                <Link to={'/home'}><a href='/home'>Home</a></Link>
                <Link to={'/dashboard'}><a href='/dashboard'>My Dashboard</a></Link>
                <Link to={'/'}><a href='/'>Logout</a></Link>
            </div>
            <div className='profileContent'>
                <h3>Update Profile</h3>
                <form action="" className='updateForm' onSubmit={updateHandler}>
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
                        <label>Confirm New Password:</label><br/>
                        <input className='input' type="text"/>
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