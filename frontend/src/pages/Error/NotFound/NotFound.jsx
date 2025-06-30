import React from 'react';
import { Button, Container, Typography, Box } from '@mui/material';
import { useNavigate } from 'react-router';

const NotFound = () => {
    const navigate = useNavigate();

    return (
        <Container component="main" maxWidth="md">
            <Box
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    justifyContent: 'center',
                    minHeight: '80vh',
                    textAlign: 'center',
                    p: 3,
                }}
            >
                <Typography variant="h1" component="h1" sx={{ fontSize: '6rem', fontWeight: 'bold', mb: 2, color: 'primary.main' }}>
                    404
                </Typography>
                <Typography variant="h4" component="h2" sx={{ mb: 3 }}>
                    Oops! Page Not Found
                </Typography>
                <Typography variant="body1" color="text.secondary" sx={{ mb: 4, maxWidth: '600px' }}>
                    The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.
                </Typography>
                <Button
                    variant="contained"
                    size="large"
                    onClick={() => navigate('/')}
                    sx={{
                        textTransform: 'none',
                        px: 4,
                        py: 1.5,
                        fontSize: '1rem',
                        borderRadius: 1,
                    }}
                >
                    Go to Homepage
                </Button>
            </Box>
        </Container>
    );
};

export default NotFound;
