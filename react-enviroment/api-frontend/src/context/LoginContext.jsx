import axios from "axios";
import { createContext, useState } from "react";
import { setCookie } from 'nookies';
import { jwtDecode } from 'jwt-decode';
import { useRouter } from "next/navigation";

export const LoginContext = createContext({LoginContextProvider})

export function LoginContextProvider({children}){
    // Public infomations for childrens components
    const [user, setUser] = useState(undefined);
    const [Awnser, setAwnser] = useState(null);
    const isAuthenticated = !!user;
    console.log(isAuthenticated);
    const router = useRouter()
 
    // Responsable to make request and set all data information
    const Login_Request = async ({ email, password }) => {
        const { message, token, valid } = await axios.post(
            "http://127.0.0.1:5000/login",
            { email, password }
        ).then(
            Awnser => {
                return Awnser.data;
            }
        );
        // Decode the payload from token

        if (valid){
            setCookie(undefined, 'blog.token', {token}, {
                maxAge: (60 * 60)
            });
            setUser(jwtDecode(token));
            router.push("/lobby");
        }
        setAwnser(<i id="status-message">{message}</i>);
    } 

    return(
        <LoginContext.Provider value={{ Login_Request, isAuthenticated, Awnser}}>
            {children}
        </LoginContext.Provider>
    )
}