'use client';

import './../style/square_style.css'
import { LoginF } from './../login-elements/login_page.js'
import { SigninF } from './../signin-elements/signin_page.js';

import { LoginContextProvider } from './../../../context/LoginContext.jsx'
import { SigninContextProvider } from './../../../context/SigninContext.jsx'
// import './../../../context/LoginContext'

import { useState } from 'react';

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
                <SigninContextProvider><SigninF ChangeMethod={ChangeMethod}></SigninF></SigninContextProvider>
            }
        </div>
    )
}
