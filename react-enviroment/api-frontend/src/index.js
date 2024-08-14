import App from './App';
import ReactDOM from 'react-dom/client';
import React from 'react';
import { Context } from './context/AuthContext.js'

const root = ReactDOM.createRoot(document.getElementById("root"))

root.render(
  <Context children={<App />} />
)