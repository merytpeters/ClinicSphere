import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import { useAuth } from '../provider/authProvider';
import { ProtectedRoute } from './ProtectedRoute';
import Signup from '../pages/StaffRegistration';
import Home from '../pages/HomePage';
import Login from '../pages/StaffLogin';
import Pharmacy from '../pages/Pharmacy';
import Appointment from '../pages/Appointment';


const Routes = () => {
    const { token } = useAuth();

    // Define public routes
    const publicRoutes = [
        {
            path: "/landingPage",
            element: <div>Landing Page</div>,
        },
        {
            path: "/about-us",
            element: <div>About Us</div>,
        },
    ];

    //Routes for non-authenticated users
    const nonAuthenticatedRoutes = [
        // Home will go in authenticated route to allow only already signed in users to generate token for other users
        {
            path: "/",
            element: <Home />,
        },
        {
            path: "/signup",
            element: <Signup />,
        },
        {
            path: "/login",
            element: <Login />,
        },
        {
            path: "/patient/login",
            element: <div>Patient Login</div>
        },
        // Pharmacy will be moved to authenticatedRoutes later
        {
            path: "/pharmacy",
            element: <Pharmacy />,
        },
        // Appointment will be moved to authenticatedRoutes later
        {
            path: "/appointments",
            element: <Appointment />,
        },
    ];

    // Routes for authenticated users
    const authenticatedRoutes = [
        {
            path: "/",
            element: <ProtectedRoute />,
            children: [
                {
                    path: "/profile",
                    element: <div>Staff Profile</div>,
                },
                {
                    path: "/logout",
                    element: <div>Logout</div>,
                },
                {
                    path: "/patient-profile",
                    element: <div>Patient Profile</div>,
                },
                {
                    path: "/patient-logout",
                    element: <div>Patient Logout</div>,
                },
            ],
        },
    ];

    // Combine routes by authentication status
    const router = createBrowserRouter([
        // Public routes visible to everyone
        ...publicRoutes,

        // Non-authenticated routes shown without token
        ...(!token ? nonAuthenticatedRoutes: []),

        // Show authenticated routes if token is present
        ...(token ? authenticatedRoutes : []),
    ]);

    // Router Configuration
    return <RouterProvider router={router} />;
};

export default Routes;