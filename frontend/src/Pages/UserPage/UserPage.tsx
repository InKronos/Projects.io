import React, { Component, ReactNode, useEffect, useState } from "react"
import { Route, Navigate, Link } from 'react-router-dom';
import NavBar from "../../Component/NavBar/NavBar";
import "./UserPage.css"
import { connect } from "react-redux";
import CustomPopup from "../../Component/CustomPopup/CustomPopup";

const UserPage = ({ }) => {

    const [profile, setProfile] = useState([]);
    const [projects, setProjects] = useState([]);
    const [loadingProfile, setLoadingProfile] = useState(true);
    const [loadingProjects, setLoadingProjects] = useState(true);
    const [error1, setError1] = useState(false);
    const [error2, setError2] = useState(false);
    const [visibility, setVisibility] = useState(false);

    const [formData, setFormData] = useState({
        password: ''
    });
    const { password } = formData;
    
    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const deleteProfile = e => {
        e.preventDefault();
        deleteProfileFun(password);
    }

    const location = window.location.pathname.split("/");

    useEffect(() => {
        getProfile();
        getProjects();
    }, []);

    const popupDeleteCloseHandler = (e) => {
        setVisibility(e);
    };


    const deleteProfileFun = (current_password) => {
        return fetch(`${process.env.REACT_APP_REMOTE_URL}/auth/users/me/`, {
            method: 'DELETE',
            mode: 'cors',
            headers:{
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`
            },
            body: JSON.stringify({ current_password })
        })
          .then(response => response.json())
          .then(responseJson => {
                localStorage.removeItem('access');
                localStorage.removeItem('refresh');
          })
          .catch(error => {
           
          });
    }

    const getProfile = () => {
        return fetch(`${process.env.REACT_APP_REMOTE_URL}/Users/api/Users/:id/`.replace(":id", location[2]), {
            method: 'GET',
            mode: 'cors',
            headers:{
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`
            }
        })
          .then(response => response.json())
          .then(responseJson => {
            setProfile([responseJson]);
            setLoadingProfile(false);
          })
          .catch(error => {
            setLoadingProfile(false);
            setError1(true);
          });
    }


    const getProjects = () => {
        return fetch(`${process.env.REACT_APP_REMOTE_URL}/Projects/api/Projects/myProjects/`, {
            method: 'GET',
            mode: 'cors',
            headers:{
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`
            }
        })
          .then(response => response.json())
          .then(responseJson => {
            setProjects(responseJson);
            setLoadingProjects(false);
          })
          .catch(error => {
            setLoadingProjects(false);
            setError2(true);
          });
    }

    return (
        <div>
            { !loadingProfile && !error1 && profile.map(profile =>
            <div id="Widget">
            
            <div id="Profile-card">
                <h1><text>User Page</text></h1>
                <img id="User-avatar" src={profile["User"]["avatar"].replace("./frontend/public/", "../")}></img>
                <div id="Name-card">
                    <h2><text>{profile["User"]["name"]}</text></h2>
                    <h3><text>EMAIL</text></h3>
                </div>
                <div id="About-field">
                    <h4><text>ABOUT</text></h4>
                    <div id="About-text">
                        <b><text>Text</text></b>
                    </div>
                </div>
            </div>

            <div id="Details-card">
                <h1><text>Details</text></h1>
                <h4>
                    <table>
                        <tr>
                            <td><text>Averange rate:</text></td>
                            <td><text></text></td>
                        </tr>
                        <tr>
                            <td> <text>Took part in:</text></td>
                            <td> <text></text></td>
                        </tr>
                        <tr>
                            <td><text>Skills:</text></td>
                            <td><text></text></td>
                        </tr>
                    </table>
                </h4>
            </div>
            { profile["isOwner"] == "True" && 
                <div id="Owner-exclusive">
                    <Link to="/user/edit" style={{ textDecoration: 'none' }}>
                        <button type="button" className="btn">Edit profile</button>
                    </Link>

                    <button type="button" className="btn">Become developer</button>
                    <button type="button" className="btn" onClick={(e) => setVisibility(!visibility)}>Delete profile</button>
                    <CustomPopup
                    onClose={popupDeleteCloseHandler}
                    show={visibility}
                    title="Delete Profile"
                    >
                        <h2>Type password to delete</h2>
                        <form onSubmit={e => deleteProfile(e)}>
                            <input type="password" name="password" className="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon2"  value={password}
                            onChange={e => onChange(e)}/>
                            <button type="submit" className="btn">YES</button>
                        </form>
                    </CustomPopup>
                </div>
            }
        </div>
            )
        }
       </div>
    );
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
})


export default connect(mapStateToProps, {})(UserPage);