import { useState } from "react";
import {send_request}  from "/src/Js/login_button_action.js";

function capture_data(){
    const email = document.getElementById(props.email.id);
    const password = document.getElementById(props.password.id);

    [emailValue, setEmail] = useState(email.value)
    [passwordValue, setPassword] = useState(password.value)
    
    send_request(emailValue, passwordValue)
}

function login(){
    return(
        <div class="login-square">
            <div class="fields">
                <input type="email" id="email-input" placeholder="Digite o seu email"/>
                <input type="password" id="password-input" placeholder="Digite a sua senha"/>
            </div>
            <div class="buttons">
                <button type="button" class="login" OnAction={send_request}{capture_data}>Login</button>
            </div>
            
        </div>
    );
}
export default login;