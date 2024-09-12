import { LoginContextProvider } from "./context/LoginContext.jsx";
import { Lobby_Content } from "./pages/Lobby/lobby_elements/lobby_content_page.js"; 

export default function Lobby(){
    <LoginContextProvider>
        <Lobby_Content />
    </LoginContextProvider>
}