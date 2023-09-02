import logo from "./logo.svg";
import "./App.css";
import ReactDOM from "react-dom/client";
import { useState } from "react";

function MyForm() {
  const [inputString, setInputString] = useState("");
  const [imageUrl, setImageUrl] = useState(null);
  const [playlistName, setPlaylistName] = useState(null);
  const [playlistOwner, setPlaylistOwner] = useState(null);
  const [playlistLength, setPlaylistLength] = useState(null);

  const sendStringToBackend = async () => {
    try {
      const response = await fetch("http://localhost:8000/send_string/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ inputString }),
      });

      const data = await response.json();

      console.log(data);
      setImageUrl(data.thumbnail_url);
      setPlaylistName(data.playlist_name);
      setPlaylistOwner(data.playlist_channel);
      setPlaylistLength(data.playlist_length);
    } catch (error) {
      console.error("There was an error sending the string:", error);
    }
  };

  return (
    <div>
      <div>
        Enter an URL: &nbsp;&nbsp;
        <input
          id="textboxid"
          value={inputString}
          onChange={(e) => setInputString(e.target.value)}
        />
        &nbsp;&nbsp;&nbsp;&nbsp;
        <button onClick={sendStringToBackend}>Send</button>
      </div>
      <div>
        {imageUrl && (
          <div>
            <img id="image" src={imageUrl} />
            <h3 id="nameDisplay">Playlist name: {playlistName}</h3>
            <h3 id="ownerDisplay">Playlist owner: {playlistOwner}</h3>
            <h3 id="lengthDisplay">Playlist length: {playlistLength}</h3>
          </div>
        )}
      </div>
    </div>
  );
}

export default MyForm;
