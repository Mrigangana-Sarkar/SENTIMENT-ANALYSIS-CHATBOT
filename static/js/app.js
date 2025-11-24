// static/js/app.js

const chatContainer = document.getElementById("chat-container");
const chatForm = document.getElementById("chat-form");
const messageInput = document.getElementById("message-input");
const summaryBtn = document.getElementById("summary-btn");
const resetBtn = document.getElementById("reset-btn");
const summaryBox = document.getElementById("summary-box");

function addMessageToUI(sender, text, sentimentLabel = null) {
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message", sender);

  const textSpan = document.createElement("span");
  textSpan.classList.add("text");
  textSpan.textContent = text;
  msgDiv.appendChild(textSpan);

  if (sender === "user" && sentimentLabel) {
    const sentSpan = document.createElement("span");
    sentSpan.classList.add("sentiment");
    sentSpan.textContent = `Sentiment: ${sentimentLabel}`;
    msgDiv.appendChild(sentSpan);
  }

  chatContainer.appendChild(msgDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = messageInput.value.trim();
  if (!text) return;

  // Show user message immediately
  addMessageToUI("user", text);

  try {
    const res = await fetch("/api/message", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    if (!res.ok) {
      console.error("Error from server");
      return;
    }

    const data = await res.json();
    const userSent = data.user_sentiment;
    const botReply = data.bot_reply;

    // Update last user message sentiment (or add a new line)
    // Simple approach: append separate line:
    const sentimentLine = `Sentiment: ${userSent.label} (score: ${userSent.compound.toFixed(2)})`;
    addMessageToUI("user", sentimentLine, null);

    // Bot reply
    addMessageToUI("bot", botReply);

  } catch (err) {
    console.error(err);
  }

  messageInput.value = "";
});

summaryBtn.addEventListener("click", async () => {
  try {
    const res = await fetch("/api/summary");
    if (!res.ok) {
      summaryBox.textContent = "Error fetching summary.";
      return;
    }

    const data = await res.json();
    summaryBox.innerHTML = `
      <h2>Overall Conversation Sentiment</h2>
      <p><strong>Label:</strong> ${data.overall_label}</p>
      <p><strong>Average score:</strong> ${data.average_compound.toFixed(2)}</p>
      <p><strong>Messages analyzed:</strong> ${data.user_message_count}</p>
      <p><strong>Trend:</strong> ${data.trend}</p>
    `;
  } catch (err) {
    console.error(err);
    summaryBox.textContent = "Error fetching summary.";
  }
});

resetBtn.addEventListener("click", async () => {
  try {
    const res = await fetch("/api/reset", {
      method: "POST"
    });
    if (!res.ok) return;

    chatContainer.innerHTML = "";
    summaryBox.innerHTML = "";
  } catch (err) {
    console.error(err);
  }
});
