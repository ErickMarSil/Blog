import { LoginContextProvider } from "../context//LoginContext.jsx";
import { Lobby_Content } from "./lobby_elements/lobby_content_page"; 


export default function Lobby(){
    <LoginContextProvider>
        <Lobby_Content />
    </LoginContextProvider>
}