import React, { Component, ReactNode, useState } from "react"
import { Route, Navigate } from 'react-router-dom';
import NavBar from "../../Component/NavBar/NavBar";
import "./LoginPage.css";
import { connect } from "react-redux";
import { FC } from "react";
import { login } from "../../Actions/auth";

const LoginPage = ({login, isAuthenticated}) => {
    const [formmData, setFormData] = useState({
        email: '',
        password: ''
    });
    const { email, password } = formmData;

    const onChange = e => setFormData({ ...formmData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();
        login(email, password);
    }

    if (isAuthenticated) {
        return <Navigate replace to="/" />
    }

    return (
        <div>
            <div>
                <div id="LoginCard">
                    <h1>WELCOME</h1>
                    <h3>Please sign in</h3>
                    <div className="input-group mb-3">
                        <form onSubmit={e => onSubmit(e)}>
                        <input type="text" className="form-control" name="email" placeholder="Email" aria-label="Project name" aria-describedby="basic-addon2" value={email}
                        onChange={e => onChange(e)}/>
                        <input type="password" name="password" className="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon2"  value={password}
                        onChange={e => onChange(e)}/>
                        
                        <button className="btn btn-outline-secondary" type="submit">Sign in</button>
                       
                        </form>
                    </div>
                </div>
            </div>
        </div >
    )
}


const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
})

export default connect(mapStateToProps, { login })(LoginPage);