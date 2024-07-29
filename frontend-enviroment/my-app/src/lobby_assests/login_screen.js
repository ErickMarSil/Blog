function login(){
    return(
        <div class="login-square">
            <div class="fields">
                <input type="email" id="email-input" placeholder="Digite o seu email"/>
                <input type="password" id="password-input" placeholder="Digite a sua senha"/>
            </div>
            <div class="buttons">
                <button type="button" class="login" action="sendrequest">Login</button>
            </div>
        </div>
    );
}
export default login;