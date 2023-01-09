import React from 'react'
import { Link } from 'react-router-dom'
import '../App.css';

const Dashboard = () => {
    return (
        <div className='dashboardContainer'>
            <div className='dashboardNavbar'>
                <Link to={'/home'}><a href='/home'>Home</a></Link>
                <Link to={'/profile'}><a href='/profile'>Profile</a></Link>
                <Link to={'/'}><a href='/'>Logout</a></Link>
            </div>
            <div className='dashboardContent'>
                <h3>Your Items:</h3>
            </div>
        </div>
    )
}

export default Dashboard