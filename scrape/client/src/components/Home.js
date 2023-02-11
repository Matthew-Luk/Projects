import {useEffect} from 'react'
import { Link } from 'react-router-dom'
import '../App.css';

const Home = (props) => {
    const {topSearches,setTopSearches,watchList,setWatchList} = props

    // const addHandler = (e) => {
    //     e.preventDefault()

    // }

    useEffect(() => {
        fetch("http://localhost:5000/top_searches")
        .then(res => res.json())
        .then(data => {
            console.log(data.top_searches)
            setTopSearches(data.top_searches)
        })
    },[])


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
                <h3>Top Searches:</h3>
                <div className='homeContentTopSearches'>
                    {
                        topSearches.map((item,index) => (
                            <div className='product-block' key={index}>
                                <h4>{item.name}</h4>
                                <img className='image' src={item.picture} alt=""/>
                                <button className='addBtn'>Add to watchlist</button>
                            </div>
                        ))
                    }
                </div>
            </div>
        </div>
    )
}

export default Home