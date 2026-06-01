import React from "react";
import "../styles/demo.css";

function DemoWebsite({ openChat }) {
  return (
    <div className="demo-container">

      <nav className="navbar">
        <h2>BeachKicks</h2>
        <div className="nav-links">
          <span>Home</span>
          <span>Shop</span>
          <span>About</span>
          <span>Contact</span>
        </div>
      </nav>

      <section className="hero">
        <h1>Step Into Summer</h1>
        <p>Premium sneakers designed for beach vibes.</p>
        <button className="shop-btn">Shop Now</button>
      </section>

      <div className="products">
        <div className="card">Wave Runner</div>
        <div className="card">SandStorm</div>
        <div className="card">Ocean Breeze</div>
      </div>

      <div className="chat-logo" onClick={openChat}>
        🤖
      </div>

    </div>
  );
}

export default DemoWebsite;
