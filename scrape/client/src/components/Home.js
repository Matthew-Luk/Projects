import {useEffect} from 'react'
import { Link } from 'react-router-dom'
import '../App.css';

const Home = (props) => {
    const {firstName,setFirstName,lastName,setLastName,email,setEmail,password,setPassword,topSearches,setTopSearches,watchList,setWatchList} = props

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

    const logoutHandler = () => {
        setFirstName("")
        setLastName("")
        setEmail("")
        setPassword("")
        console.log("logged out")
    }

    return (
        <div className='homeContainer'>
            <div className='homeNavbar'>
                <Link to={'/dashboard'}>My Dashboard</Link>
                <Link to={'/profile'}>Profile</Link>
                <Link to={'/'} onClick={logoutHandler}>Logout</Link>
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