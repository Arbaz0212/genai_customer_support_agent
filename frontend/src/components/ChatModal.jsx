import React, { useState, useEffect, useRef } from "react";

const ChatModal = ({ onClose }) => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isClosing, setIsClosing] = useState(false);
  const chatEndRef = useRef(null);

  // Auto scroll to bottom
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = {
      role: "user",
      text: input,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();

      const botMessage = {
        role: "bot",
        text: data.response || "No response from server.",
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "bot",
          text: "Server error. Please try again.",
        },
      ]);
    }
  };

const handleClose = () => {
  setIsClosing(true);

  setTimeout(() => {
    onClose();   // unmount AFTER animation
  }, 300); // match CSS animation duration
};

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="modal-overlay">
      <div className={`chat-modal ${isClosing ? "closing" : ""}`}>

        {/* HEADER */}
        <div className="chat-header">
          <span>AI Customer Support</span>
          <button onClick={handleClose} style={{ background: "none", border: "none", color: "white", cursor: "pointer" }}>
            ✕
          </button>
        </div>

        {/* CHAT BODY */}
        <div className="chat-body-only">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={msg.role === "user" ? "user-msg" : "bot-msg"}
            >
              {msg.text}
            </div>
          ))}
          <div ref={chatEndRef} />
        </div>

        {/* INPUT */}
        <div className="chat-input">
          <input
            type="text"
            placeholder="Ask your question..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyPress}
          />
          <button onClick={handleSend}>Send</button>
        </div>

      </div>
    </div>
  );
};

export default ChatModal;
