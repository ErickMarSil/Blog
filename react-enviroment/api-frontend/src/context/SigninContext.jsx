import axios from "axios";
import { createContext } from "react";

export const SigninContext = createContext({SigninContextProvider})

export function SigninContextProvider({ children }){
    
    const Signin_Request = async ({ first_name, last_name, email, password, birth_date, nickname }) => {
        // const nav = useNavigate();
        const {message, redirect, valid} =  axios.post(
            "http://127.0.0.1:5000/signin",
            {
                first_name,
                last_name,
                email,
                password,
                birth_date,
                nickname
            }
        ).then(
            awnser => {
                return awnser.data;
            }
        )
        
        return redirect;
    }
    
    return(
        <SigninContext.Provider value={{Signin_Request}}>
            {children}
        </SigninContext.Provider>
    )
}