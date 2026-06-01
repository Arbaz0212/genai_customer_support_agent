return (
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
);
