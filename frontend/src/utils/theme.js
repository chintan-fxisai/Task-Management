import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#2d2d2d',
      contrastText: '#fff',
    },
    secondary: {
      main: '#8c8c8c',
    },
    link: {
      main: '#5770ef',
    },
    background: {
      default: '#f5f5f5',
      paper: '#ffffff',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
  },
  shape: {
    borderRadius: 8,
  },

});

export default theme;