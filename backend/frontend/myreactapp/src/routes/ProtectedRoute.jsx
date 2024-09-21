import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from "../provider/authProvider";

export const ProtectedRoute = () => {
    const { token } = useAuth();

    // Check that user is authenticated
    if (!token) {
        // Redirect to login
        return <Navigate to="/login" />;
    }

    // if authenticated render the child routes
    return <Outlet />;
};