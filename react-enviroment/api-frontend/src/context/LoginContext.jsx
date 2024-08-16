import axios from "axios";
import { createContext, useState } from "react";

export const LoginContext = createContext({LoginContextProvider})

export function LoginContextProvider({children}){

    const [userInfos, setUserInfos] = useState({})

        const Login_Request = async ({ email, password }) => {
            return axios.post(
                "http://127.0.0.1:5000/login",
                { email, password }
            ).then(
                awnser => {
                    return awnser.data;
                }
            ).catch(
                console.log("wasn´t able to connect with the server")
            )
        } 

    return(
        <LoginContext.Provider value={{Login_Request, userInfos}}>
            {children}
        </LoginContext.Provider>
    )
}