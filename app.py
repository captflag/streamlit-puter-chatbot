import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 Interactive AI Chatbot with Puter.js")
st.markdown("Enjoy a smoother chat experience with loading feedback and scrollable responses.")

components.html("""
<!DOCTYPE html>
<html>
<head>
  <script src="https://js.puter.com/v2/"></script>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      padding: 1rem;
      background: #f0f2f5;
    }
    #chatbox {
      width: 100%;
      max-width: 600px;
      margin: auto;
      text-align: center;
    }
    input, button {
      padding: 0.6rem;
      margin-top: 1rem;
      width: 100%;
      font-size: 1rem;
      border-radius: 5px;
      border: 1px solid #ccc;
    }
    button {
      background-color: #007bff;
      color: white;
      cursor: pointer;
    }
    button:disabled {
      background-color: #aaa;
      cursor: not-allowed;
    }
    #response {
      margin-top: 1rem;
      background: #fff;
      padding: 1rem;
      border-radius: 5px;
      box-shadow: 0 0 5px rgba(0,0,0,0.1);
      white-space: pre-wrap;
      text-align: left;
      max-height: 300px;
      overflow-y: auto;
    }
    #loading {
      display: none;
      margin-top: 1rem;
      font-style: italic;
      color: #555;
    }
  </style>
</head>
<body>
  <div id="chatbox">
    <h3>Talk to GPT-5 Nano</h3>
    <input id="prompt" placeholder="Type your message..." />
    <button id="sendBtn" onclick="send()">Send</button>
    <div id="loading">⏳ Thinking...</div>
    <div id="response"></div>
  </div>

  <script>
    async function send() {
      const prompt = document.getElementById("prompt").value;
      const btn = document.getElementById("sendBtn");
      const loading = document.getElementById("loading");
      const responseBox = document.getElementById("response");

      if (!prompt.trim()) return;

      btn.disabled = true;
      loading.style.display = "block";
      responseBox.innerText = "";

      try {
        const response = await puter.ai.chat(prompt, { model: "gpt-5-nano" });
        const reply = response?.content || response?.message?.content || "No reply received.";
        responseBox.innerText = reply;
      } catch (err) {
        responseBox.innerText = "Error: " + err.message;
      }

      btn.disabled = false;
      loading.style.display = "none";
    }
  </script>
</body>
</html>
""", height=650)



