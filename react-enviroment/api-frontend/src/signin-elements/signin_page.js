import './signin_style.css'
import { useForm } from 'react-hook-form';

export function SigninF(){

    const { register, handleSubmit } = useForm();

    const SiginRequest = (e) =>{
        e.preventDefault();
        console.log("logged")
    }

    const form_element = (
        <div>
            <form id="signin-form">
                <div className='name'>
                    <p>Place your name information</p>
                    <input type='text' placeholder='First name'/>
                    <br></br>
                    <input type='text' placeholder='Last name'/>
                    <br></br>
                    <p>How whould you´d like to call?</p>
                    <input type='text' placeholder='Nick name'/>
                </div>
                <div className='email'>
                    <p>Place your email information</p>
                    <input {...register('email')} type="email" placeholder="Email" />
                </div>
                <div className='password'>
                    <p>Place your password information</p>
                    <input {...register('password')} type="password" placeholder="Enter your password" />
                    <br></br>
                    <input type="password" placeholder="Confirm your password" />
                </div>
                <div>
                    <p></p>
                    <input type='date'/>
                </div>
                <button type='submit' onClick={(e) => {SiginRequest(e)}}>Cadastrar</button>
            </form>
        </div>
    );

    return form_element;
} 