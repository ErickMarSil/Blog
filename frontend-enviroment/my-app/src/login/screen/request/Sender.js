import axios from 'axios';
import { useEffect, useState } from 'react';

export function SendRequestLogin(){
    const [userInformations, setUserInformations] = useState({});
    const getInformations = async () =>{
        const infroamtionList = axios.post(
            "http://127.0.0.1:5000",
            () => {
                return(
                    {
                    "type": "login", 
                    "email": document.getElementById("fragment-email").value, 
                    "password":document.getElementById("fragment-password").value
                });}
        )
    }
    return(
        ""
    );
}