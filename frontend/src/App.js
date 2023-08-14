import logo from './logo.svg';
import './App.css';
import ReactDOM from 'react-dom/client';
import { useState } from 'react';



function MyForm() {
  const [inputString, setInputString] = useState('');

const sendStringToBackend = async () => {
    try {
        const response = await fetch('http://localhost:8000/send_string/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputString }),
        });

        const data = await response.json();

        console.log(data);
    } catch (error) {
        console.error("There was an error sending the string:", error);
    }
};

return (
    <div>
      Enter an URL: &nbsp;&nbsp;
        <input
            id="textboxid"
            value={inputString}
            onChange={(e) => setInputString(e.target.value)}
        />&nbsp;&nbsp;&nbsp;&nbsp;
        <button onClick={sendStringToBackend}>Send</button>
    </div>
);
}

export default MyForm;
