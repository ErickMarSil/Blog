import axios from "axios";
import { createContext } from "react";

export const SigninContext = createContext({SigninContextProvider})

export function SigninContextProvider({ children }){
    async function Signin_Request({ first_name, last_name, email, password, birth_date, nickname }){
        const awnser = await axios.post(
            "http://127.0.0.1:5000/signin",
            {
                first_name,
                last_name,
                email,
                password,
                birth_date,
                nickname
            }
        );
        console.log(awnser);
    }

    return(
        <SigninContext.Provider value={{Signin_Request}}>
            {children}
        </SigninContext.Provider>
    )
}