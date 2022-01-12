import { Component, ReactNode, useState } from "react"
import { Link } from "react-router-dom";
import { Card } from "reactstrap";

export interface Project{
    id: number,
    title: string,
    stage: string,
    description: string,
    folder: string,
    averageRate: string,
    idOwner: number
}

class SearchProject extends Component{
    
    state = {
        projects: [] ,
        loading: true,
        error: false
      }
    

    componentWillMount(){
        this.getObject();
    }
    
    getObject(){
        return fetch(`${process.env.REACT_APP_REMOTE_URL}/Projects/api/Projects/`, {
            method: 'GET',
            mode: 'cors',
            headers:{
                'Content-Type': 'application/json'
            }
        })
          .then(response => response.json())
          .then(responseJson => this.setState ({
              projects: responseJson,
              loading: false
          }))
          .catch(error => this.setState ({
            error: true,
            loading: false
        }));
    }

    render(): ReactNode {
        const { projects, loading, error } = this.state;
        return(
            <div>
                
                {loading && <div>Loading...</div>}
                {!loading && !error && projects.map(project => 
                <div className="card-body">
                    <h2 className="card-title">{project["Project"]["title"]}</h2>
                    <p className="card-text">Author: {project["Meneger"]}</p>
                    <Link to={"/Projects/"+project["Project"]["pk"]} style={{ textDecoration: 'none' }}>
                        <button className="btn btn-outline-secondary" type="button">Show</button>
                    </Link>
                </div>)
                }
                {error && <div>Error message</div>}
            </div>
        )
    }
}


export default SearchProject;