import React from 'react';
import { useEffect } from 'react';
// import { createConnection } from 
import ReactDOM from 'react-dom/client';
import Login from './lobby_assests/login_screen';
import reportWebVitals from './reportWebVitals';

// function conx(){
//   return{
//     useEffect(())
//   }
// }

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Login />
  </React.StrictMode>
);

reportWebVitals();