import React, { Component, ReactNode, useState } from "react"
import { Route, Navigate } from 'react-router-dom';
import "./CreateProject.css";
import { connect } from "react-redux";
import { deepEqual } from "assert";

const CreateProject = ({isAuthenticated, user}) => {
    const [formData, setFormData] = useState({
        title: '',
        description: ''
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(false);

    const { title, description } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();
        postObject();
    }

    const postObject = () => {
        return fetch('http://127.0.0.1:8000/Projects/api/Projects/', {
            method: 'POST',
            mode: 'cors',
            headers:{
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`
            },
            body: JSON.stringify({ title, description })
        })
          .then(response => response.json())
          .then(responseJson => {
            setLoading(true);
          })
          .catch(error => {
            setLoading(false);
            setError(true);
          });
    }

    if (!isAuthenticated) {
        //return <Navigate replace to="/" /> TO DO nie wiem jak to naprawić
    }

    return (
        <div>
            <div>
                <div id="LoginCard">
                    <h1>Create Project</h1>
                    <h3></h3>
                    <div className="input-group mb-3">
                        <form onSubmit={e => onSubmit(e)}>
                        <input type="text" className="form-control" name="title" value={title} onChange={e => onChange(e)} placeholder="Title of the project" aria-label="Project name" aria-describedby="basic-addon2"/>
                        <textarea placeholder="description" name="description" value={description} onChange={e => onChange(e)}></textarea>
                        
                        <button className="btn btn-outline-secondary" type="submit">Create</button>
                       
                        </form>
                    </div>
                </div>
            </div>
        </div >
    )
}


const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated,
    user: state.auth.user
})

export default connect(mapStateToProps)(CreateProject);