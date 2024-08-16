import { LoginF } from './login-elements/login_page.js'
import { SigninF } from './signin-elements/signin_page.js';

import { useState } from 'react';

import { LoginContextProvider } from './context/LoginContext.jsx'
import { SigninContextProvider } from './context/SigninContext.jsx'

export default function App(){
    const [method, setMethod] = useState("Login")

    function ChangeMethod(){
        setMethod(prevMethod => (prevMethod === "Login" ? "Signin" : "Login"))
    }
    return  (
        <div className='FullForm'>
            <button type='button' onClick={ChangeMethod}> Faça o seu {method} </button>
            {method === "Login" ? 
                <LoginContextProvider><LoginF /></LoginContextProvider>:
                <SigninContextProvider><SigninF /></SigninContextProvider>
            }
        </div>
    )
}