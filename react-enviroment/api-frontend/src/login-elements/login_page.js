import './login_style.css'

export function Fields(){
    const form_element = (
        <div>
            <form id="login-form">
                <p>Place your credentials in fields bellow</p>
                <input type="text" placeholder="Enter your email"></input>
                <br></br>
                <input type="text" placeholder="Enter your password"></input>
                <br></br>
                <a href="#">Forgot your password?</a>
                <br></br>
                <input type="submit"></input>
            </form>
        </div>
    );
    triggedForm(form_element);

    return form_element;
}

function triggedForm (form){
    form.addEventListener("submit", action());
}

function action(){
    console.log("printed");
}