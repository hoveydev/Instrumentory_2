import { Navigate } from "react-router-dom";
import { useContext } from "react";
import AuthContext from "../context/AuthContext";


const LoggedInRoute = ({ children }) => {
    let {user} = useContext(AuthContext);
    return user ? <Navigate to='/dashboard' /> : children;
}

export default LoggedInRoute