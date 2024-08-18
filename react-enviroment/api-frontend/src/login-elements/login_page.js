import { useForm } from "react-hook-form";
import { useContext } from "react";
import { LoginContext } from '../context/LoginContext';

export function LoginF(){
    const { register, handleSubmit } = useForm();
    const { Login_Request, awnser } = useContext(LoginContext);

    async function LoginAction (data){
        await Login_Request(data);
    }

    const form_element = (
        <>
            <div>
                {awnser}
                <form id="login-form" onSubmit={handleSubmit(LoginAction)}>
                    <p>Place your credentials in fields bellow</p>
                    <input {...register('email')} type="text" placeholder="Enter your email"></input>
                    <br></br>
                    <input {...register('password')} type="password" placeholder="Enter your password"></input>
                    <br></br>
                    <a href="#">Forgot your password?</a>
                    <br></br>
                    <button type='submit'>Logar</button>
                </form>
            </div>
        </>
        
    );

    return form_element;
}