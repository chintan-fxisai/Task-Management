import React from 'react';
import { Button } from '@mui/material';
import { useNavigate } from 'react-router';
import { toast } from 'react-toastify';
import { useDispatch } from 'react-redux';
import { logout } from '../../redux/Slices/AuthSlice';

const LogoutButton = () => {
    const navigate = useNavigate();
    const dispatch = useDispatch();

    const handleLogout = () => {
        dispatch(logout());

        // Show success message
        toast.success('Logged out successfully');

        // Navigate to login page
        navigate('/login');

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