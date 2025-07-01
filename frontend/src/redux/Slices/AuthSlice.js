import { createSlice } from "@reduxjs/toolkit";

const token = localStorage.getItem('access_token');
const user = localStorage.getItem('user');
const is_active = localStorage.getItem('user') ? true : false;

const initialState = {
    token: token || null,
    user: user || null,
    is_registered: false,
    isAuthenticated: is_active,
    is_active: is_active,
}

export const AuthSlice = createSlice({

    name: "auth",
    initialState,
    reducers: {
        
        login_success(state, action){
            state.token = action.payload.token;
            state.user = action.payload.user;
            state.isAuthenticated = true;
            state.is_active = true;
        },

        login_fail(state){
            state.token = null;
            state.user = null;
            state.isAuthenticated = false;
            state.is_active = false;
        },

        logout(state){
            localStorage.clear();
            state.token = null;
            state.user = null;
            state.is_active = false;
        },

        register_success(state){
            state.is_registered = true;
        },

        register_fail(state){
            state.is_registered = false;
        }, 
    }
})

export const {login_success, login_fail, logout, register_success, register_fail} = AuthSlice.actions

export default AuthSlice.reducer