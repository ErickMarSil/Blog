import axios from "axios";
import { createContext } from "react";

export const SigninContext = createContext({SigninContextProvider})

export function SigninContextProvider({ children }){
    async function Signin_Request(data){
        axios.post
    }

    return(
        <SigninContext.Provider value={{Signin_Request}}>
            {children}
        </SigninContext.Provider>
    )
}