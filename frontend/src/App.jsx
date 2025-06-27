import './App.css'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router'
import { Signup } from './components/Signup';
import { Login } from './components/Login';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </Router>
  );
}

export default App;
