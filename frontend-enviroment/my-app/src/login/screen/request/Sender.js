import axios from "axios"

function send_request(){
    const getContent = () =>{
        return(
            {
                "type":"login",
                "email": document.getElementById("fragment-email"),
                "password": document.getElementById("fragment-password")
            }
        )
    }
    const awnser = axios.post(
        "http://127.0.0.1:5000",
        getContent()
    )
}

export default send_request();