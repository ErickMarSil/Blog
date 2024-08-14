import './signin_style.css'
import { useForm } from 'react-hook-form';

export function SigninF(){

    const { register, handleSubmit } = useForm();

    const SiginRequest = (e) =>{
        e.preventDefault();
        console.log("logged")
    }

    function SigninAction (data){
        console.log(data);
    }

    const form_element = (
        <div>
            <form id="signin-form" onSubmit={handleSubmit(SigninAction)}>
                <div className='name'>
                    <p>Place your name information</p>
                    <input {...register('first_name')} type='text' placeholder='First name'/>
                    <br></br>
                    <input {...register('last_name')} type='text' placeholder='Last name'/>
                    <br></br>
                    <p>How whould you´d like to call?</p>
                    <input {...register('nickname')} type='text' placeholder='Nick name'/>
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
                    <p>Select your birth date</p>
                    <input {...register('birth_date')} type='date'/>
                </div>
                <button type='submit'>Cadastrar</button>
            </form>
        </div>
    );

    return form_element;
} 