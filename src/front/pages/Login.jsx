import React, { useEffect, useState } from "react"
import rigoImageUrl from "../assets/img/rigo-baby.jpg";
import useGlobalReducer from "../hooks/useGlobalReducer.jsx";

export const Login = () => {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const token = sessionStorage.getItem("token");

    console.log("this is your token:"+token)

    const handleClick = () => {
        const opts = {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "email": email,
                "password": password
            })
        }
    
        fetch("https://effective-telegram-97jjq94957rxh7j6v-3001.app.github.dev/api/login", opts)
        .then(resp => {
            if(resp.status === 200) return resp.json();
            else alert("There was an error with the response")
        })
        .then(data => {
            console.log("this came from the backend:", data)
            sessionStorage.setItem("token",data.token);
        })
        .catch(error => {
            console.error("There was an error", error)
        })
    }

    return (
        <div className="text-center mt-5">
            {(token && token!="" && token!=undefined) ? "Your are logged in with this token:"+token :            
                <form action={handleClick}>
                    <label for="email">Email:</label>
                    <input type="text" id="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)}/><br /><br />
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}/><br /><br />
                    <input type="submit" value="Login" />
                </form>
            }
        </div>
    );
}; 