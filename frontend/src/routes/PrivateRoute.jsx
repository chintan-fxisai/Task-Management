import React from 'react';
import { is_active } from '../services/authServices';
import { Navigate } from 'react-router';
import { toast } from 'react-toastify';

const PrivateRoute = ({ children }) => {
    const isAuthenticated = is_active();

    if (!isAuthenticated) {
        // Redirect to login if not authenticated
        return <Navigate to="/login" replace />;
    }

    return children;
};

export default PrivateRoute;