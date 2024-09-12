import { LoginContext } from '../../../context/LoginContext';
import { useContext } from 'react';
import { notFound } from 'next/navigation';

export function Lobby_Content(){
    const { isAuthenticated, Awnser, Login_Request } = useContext(LoginContext);
    console.log(isAuthenticated);
    console.log(Awnser);
    console.log(Login_Request);
    if (isAuthenticated) { return notFound }
    return (
        <>
            <h1>dashboard</h1>
        </>
    )
}