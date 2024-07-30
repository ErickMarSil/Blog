import axios from "axios"

const msgError = "some fields is empty!"

export function send_request(){
    const getContent = () =>{
        const empty = (document.getElementById("fragment-email").value == "") && (document.getElementById("fragment-password").value == "")
        if (empty){return msgError}

        return(
            {
                "type":"login",
                "email": document.getElementById("fragment-email").value,
                "password": document.getElementById("fragment-password").value
            }
        )
    }
    const jsonReturn = getContent()
    if (jsonReturn == msgError){
        return msgError
    }

    const awnser = axios.post(
        "http://127.0.0.1:5000/lobby",
        jsonReturn
    )
}