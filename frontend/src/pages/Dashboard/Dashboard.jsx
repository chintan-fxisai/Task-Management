import React from 'react';
import { Box, Typography, Container, Paper } from '@mui/material';
import LogoutButton from '../../components/LogoutButton';

const Dashboard = () => {
  return (
    <Box sx={{ minHeight: '100vh', backgroundColor: '#f5f5f5' }}>
      <Paper 
        elevation={3} 
        sx={{ 
          p: 2, 
          display: 'flex', 
          justifyContent: 'space-between',
          alignItems: 'center',
          mb: 4
        }}
      >
        <Typography variant="h5" component="h1">
          Task Management Dashboard
        </Typography>
        <LogoutButton />
      </Paper>
      
      <Container maxWidth="lg">
        <Paper sx={{ p: 4 }}>
          <Typography variant="h6" gutterBottom>
            Welcome to your dashboard!
          </Typography>
          <Typography variant="body1">
            This is your personal task management space. You can start managing your tasks here.
          </Typography>
        </Paper>
      </Container>
    </Box>
  );
};

export default Dashboard;