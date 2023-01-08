import React, { useEffect } from 'react'
import '../App.css';

const Home = () => {

    return (
        <div>
            <div className='homeContainer'>
                <div className='homeNavbar'>
                    <a href="">My Dashboard</a>
                    <a href="">Log Out</a>
                    <a href="">Settings</a>
                </div>
                <div className='homeSearchBar'>
                    <input type="text"/>
                    <input type="submit" value="Search"/>
                </div>
                <div className='homeContent'>
                </div>
            </div>
        </div>
    )
}

export default Home