import axios from "axios";
import { createContext, useState } from "react";
import { setCookie } from 'nookies';
import { jwtDecode } from 'jwt-decode';

export const LoginContext = createContext({LoginContextProvider})

export function LoginContextProvider({children}){
    // Public infomations for childrens components
    const [user, setUser] = useState(undefined);
    const [awnser, setAwnser] = useState(null);
    const isAuthenticated = !!user;

    // Responsable to make request and set all data information
    const Login_Request = async ({ email, password }) => {
        const { message, token, valid } = await axios.post(
            "http://127.0.0.1:5000/login",
            { email, password }
        ).then(
            awnser => {
                return awnser.data;
            }
        );

        setCookie(undefined, 'blog.token', {token}, {
            maxAge: (60 * 60)
        });
        
        // Decode the payload from token

        if (valid){
            const payload = jwtDecode(token);
            setUser(payload);
            /* redirect to main page */
        }
        setAwnser(<i id="status-message">{message}</i>);
    } 

    return(
        <LoginContext.Provider value={{ Login_Request, isAuthenticated, awnser}}>
            {children}
        </LoginContext.Provider>
    )
}