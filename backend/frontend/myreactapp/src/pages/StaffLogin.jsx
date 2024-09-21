import { useNavigate } from "react-router-dom";

const Login = () => {
    const { setToken } = useAuth();
    const navigate = useNavigate();

    const handleLogin = () => {
        setToken
    };

    return (
        <div>
            <h1>Login</h1>
            <button onClick={handleLogin}>Login</button>
        </div>
    );
};

export default Login