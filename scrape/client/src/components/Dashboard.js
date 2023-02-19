import React from 'react'
import { Link } from 'react-router-dom'
import '../App.css';

const Dashboard = () => {
    return (
        <div className='dashboardContainer'>
            <div className='dashboardNavbar'>
                <Link to={'/home'}>Home</Link>
                <Link to={'/profile'}>Profile</Link>
                <Link to={'/'}>Logout</Link>
            </div>
            <div className='dashboardContent'>
                <h3>Your Watchlist:</h3>
            </div>
        </div>
    )
}

export default Dashboard