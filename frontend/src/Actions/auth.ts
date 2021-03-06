import axios from "axios";
import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    USER_LOADED_SUCCESS,
    USER_LOADED_FAIL,
    AUTHENTICATED_SUCCESS,
    AUTHENTICATED_FAIL,
    LOGOUT,
    SIGNUP_SUCCESS,
    SIGNUP_FAIL
} from "./types"



export const load_user = () => async dispatch => {
    if(localStorage.getItem("access")){
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `JWT ${localStorage.getItem('access')}`,
                'Accept': 'application/json'
            }
        }; 

        try {
            const res = await axios.get(`${process.env.REACT_APP_REMOTE_URL}/Users/api/Users/myData/`, config);
    
            dispatch({
                type: USER_LOADED_SUCCESS,
                payload: res.data
            });
        } catch (err) {
            dispatch({
                type: USER_LOADED_FAIL
            });
        }
    } else {
        dispatch({
            type: USER_LOADED_FAIL
            
        });
    }
}

export const checkAuthenticated = () => async dispatch => {
    if (localStorage.getItem('access')) {
        const config = {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        }; 

        const body = JSON.stringify({ token: localStorage.getItem('access') });

        try {
            const res = await axios.post(`${process.env.REACT_APP_REMOTE_URL}/auth/jwt/verify/`, body, config)

            if (res.data.code !== 'token_not_valid') {
                dispatch({
                    type: AUTHENTICATED_SUCCESS
                });
            } else {
                dispatch({
                    type: AUTHENTICATED_FAIL
                });
            }
        } catch (err) {
            dispatch({
                type: AUTHENTICATED_FAIL
            });
        }

    } else {
        dispatch({
            type: AUTHENTICATED_FAIL
        });
    }
};

export const login = (email: string, password: string) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json',
            
        }
    };

    const body = JSON.stringify({ email, password });

    try {
        const res = await axios.post(`${process.env.REACT_APP_REMOTE_URL}/auth/jwt/create/`, body, config);

        dispatch({
            type: LOGIN_SUCCESS,
            payload: res.data
        });

        dispatch(load_user());
    } catch (err) {
        dispatch({
            type: LOGIN_FAIL,
            payload: err.response.data
        })
    }
};

export const signup = (name: string, email: string, password: string, re_password: string) => async dispatch => {
    const config = {
        headers: {
            'Content-Type': 'application/json'
        }
    };

    const body = JSON.stringify({ name, email, password, re_password });

    try {
        const res = await axios.post(`${process.env.REACT_APP_REMOTE_URL}/auth/users/`, body, config);
        dispatch({
            type: SIGNUP_SUCCESS,
            payload: res.data
        });
    } catch (err) {
        dispatch({
            type: SIGNUP_FAIL,
            payload: err.response.data
        })
    }
};

export const logout = () => dispatch => {
    dispatch({
        type: LOGOUT
    });
};