import api from './api';

export const getSignupList = async () => {
    try {
        const response = await api.get('/signup/');
        return response.data;
    } catch (error) {
        throw error.response.data
    }
};