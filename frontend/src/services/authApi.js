import api from "./api";

// Auth API calls
const authAPI = {
    register_user: async (userData) => {
        try {
            const response = await api.post('/register', userData);
            return {
                success: true,
                data: response.data
            };
        } catch (error) {
            return {
                success: false,
                message: error.response?.data?.detail || 'Registration failed. Please try again.'
            };
        }
    },

    login_user: async (userData) => {
        try {
            const response = await api.post('/login', userData);
            return {
                success: true,
                data: response.data
            };
        } catch (error) {
            return {
                success: false,
                message: error.response?.data?.detail || 'Login failed. Please check your credentials.'
            };
        }
    }
};

export default authAPI;