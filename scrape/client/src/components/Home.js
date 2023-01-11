import React from 'react'
import { Link } from 'react-router-dom'
import '../App.css';

const Home = () => {

    return (
        <div className='homeContainer'>
            <div className='homeNavbar'>
                <Link to={'/dashboard'}><a href='/dashboard'>My Dashboard</a></Link>
                <Link to={'/profile'}><a href='/profile'>Profile</a></Link>
                <Link to={'/'}><a href='/'>Logout</a></Link>
            </div>
            <div className='homeSearchBar'>
                <input id='searchBar' type="text" placeholder='Search...'/>
                <input type="submit" value="Search"/>
            </div>
            <div className='homeContent'>
                <h3>Top Searches</h3>
            </div>
        </div>
    )
}

export default Home