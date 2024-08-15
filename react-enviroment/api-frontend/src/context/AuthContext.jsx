import { createContext } from "react";
import axios from "axios";

export const contextObj = createContext({})

export function Context({ children }){

    const isAuthenticated = false;
    const paternUrl = "http://127.0.0.1:5000/";

    async function Login_Request({email, password}){
        const awnser = await axios.post(
            paternUrl + "login",
            {
                email,
                password
            }
        )

        console.log(awnser);
    }
    async function Signin_Request({first_name, last_name, email, password, birth_date, nickname}){
        const awnser = await axios.post(
            paternUrl + "signin",
            {
                first_name,
                last_name,
                email,
                password,
                birth_date,
                nickname
            }
        )
        
        console.log(awnser);
    }

    return(
        <contextObj.Provider value={{ isAuthenticated, Login_Request, Signin_Request }}>
            {children}
        </contextObj.Provider>
    )
}