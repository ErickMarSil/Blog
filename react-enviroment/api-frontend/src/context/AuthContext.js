import { createContext } from "react";

export const contextObj = createContext({})

export function Context({ children }){
    return(
        <contextObj.Provider value={{}}>
            {children}
        </contextObj.Provider>
    )
}