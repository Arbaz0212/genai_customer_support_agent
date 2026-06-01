import React, { useState } from "react";
import "./styles/demo.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [showChat, setShowChat] = useState(false);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userQuery = input;
    setInput("");
    setLoading(true);

    setMessages(prev => [...prev, { role: "user", text: userQuery }]);

    try {
      const response = await fetch("http://127.0.0.1:8000/ai/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userQuery })
      });

      const reader = response.body.getReader();
      const decoder = new TextDecoder("utf-8");

      let botText = "";

      setMessages(prev => [...prev, { role: "bot", text: "" }]);

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        botText += decoder.decode(value, { stream: true });

        setMessages(prev => {
          const updated = [...prev];
          updated[updated.length - 1].text = botText;
          return updated;
        });
      }

    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="demo-container">

      {/* NAVBAR */}
      <nav className="navbar">
        <h2>BeachKicks</h2>
        <div className="nav-links">
          <span>Home</span>
          <span>Shop</span>
          <span>About</span>
          <span>Contact</span>
        </div>
      </nav>

      {/* HERO SECTION */}
      <section className="hero">
        <h1>Step Into Summer</h1>
        <p>Premium sneakers inspired by beach vibes.</p>
        <button className="shop-btn">Shop Now</button>
      </section>

      {/* PRODUCTS */}
      {/* PRODUCTS */}
<div className="products">
  <div className="card">
    <img src="/images/shoe1.jpg" alt="Wave Runner" />
    <h3>Wave Runner</h3>
  </div>

  <div className="card">
    <img src="/images/shoe2.jpg" alt="SandStorm" />
    <h3>SandStorm</h3>
  </div>

  <div className="card">
    <img src="/images/shoe3.jpg" alt="Ocean Breeze" />
    <h3>Ocean Breeze</h3>
  </div>
</div>

      {/* FLOATING AI LOGO */}
      <div className="chat-logo" onClick={() => setShowChat(true)}>
        🤖
      </div>

      {/* CHAT MODAL */}
      {showChat && (
        <div className="modal-overlay">
          <div className="chat-modal">

            <div className="chat-header">
              <span>AI Customer Support Agent</span>
              <button onClick={() => setShowChat(false)}>✖</button>
            </div>

            <div className="chat-body-only">
              {messages.map((msg, i) => (
                <div
                  key={i}
                  className={msg.role === "user" ? "user-msg" : "bot-msg"}
                >
                  {msg.text}
                </div>
              ))}
            </div>

            <div className="chat-input">
              <input
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask your question..."
                onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              />
              <button onClick={sendMessage} disabled={loading}>
                {loading ? "Thinking..." : "Send"}
              </button>
            </div>

          </div>
        </div>
      )}

    </div>
  );
}

export default App;
