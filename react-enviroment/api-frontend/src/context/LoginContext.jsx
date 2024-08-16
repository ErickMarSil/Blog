import { createContext } from "react";

export const LoginContext = createContext({LoginContextProvider})

export function LoginContextProvider({children}){
    async function Login_Request(data){
        console.log(data);
    }

    return(
        <LoginContext.Provider value={{Login_Request}}>
            {children}
        </LoginContext.Provider>
    )
}