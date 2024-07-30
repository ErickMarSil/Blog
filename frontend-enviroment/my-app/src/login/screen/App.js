import {send_request} from './request/Sender.js'

function App(){
  return(
    <div>
      <input type="email" id="fragment-email" name="email" placeholder="enter your email:"/>
      <input type="password" id="fragment-password" name="password" placeholder="enter your password:"/>
      <button type="button" placeholder="submit" onClick={send_request}>submit</button>
    </div>
  )
}
export default App;