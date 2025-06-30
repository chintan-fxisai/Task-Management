import React from 'react';
import { Button } from '@mui/material';
import { useNavigate } from 'react-router';
import { toast } from 'react-toastify';
import { clear_localestorage } from '../../services/authServices';

const LogoutButton = ({ onLogout }) => {
    const navigate = useNavigate();

    const handleLogout = () => {
        // Remove user data from localStorage
        clear_localestorage();

        // Show success message
        toast.success('Logged out successfully');

        // Navigate to login page
        navigate('/login');

        // Call the onLogout callback if provided
        if (onLogout && typeof onLogout === 'function') {
            onLogout();
        }
    };

    return (
        <Button
            variant="outlined"
            color="error"
            onClick={handleLogout}
            sx={{
                textTransform: 'none',
                borderRadius: 1,
                px: 2,
                py: 1,
                '&:hover': {
                    backgroundColor: 'error.light',
                    color: 'white',
                },
            }}
        >
            Logout
        </Button>
    );
};

export default LogoutButton;