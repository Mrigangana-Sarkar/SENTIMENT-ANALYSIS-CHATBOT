# Chatbot with Sentiment Analysis — Full-Stack Python Web App

## 📌 Project Overview
This project is a **full-stack Python web application** that enables users to chat with an AI-powered bot while receiving **real-time sentiment analysis** of their messages. The system identifies whether each message is **Positive**, **Neutral**, or **Negative**, and also evaluates the **overall emotional trend** throughout the conversation — determining whether the user’s mood is improving, stable, or declining.

The chatbot tailors its responses based on the user’s sentiment, creating an emotionally intuitive conversational system.

The project fulfills both:
- **Tier 1:** Overall conversation sentiment analysis
- **Tier 2:** Per-message sentiment evaluation and mood-trend insights

---

## 🧠 Tools & Technologies Used

### 🔹 Python
Primary programming language used for backend logic and chatbot functionality.

### 🔹 Flask (Backend Framework)
A lightweight, high-performance Python web framework used to:
- Handle REST API communication between frontend and backend
- Manage user session data for conversation storage
- Serve the chat webpage

### 🔹 NLTK (Natural Language Toolkit)
A powerful NLP library used for sentiment processing.  
We specifically utilize **VADER (Valence Aware Dictionary and sEntiment Reasoner)**, which:
- Is highly effective for social media and chat-style text
- Returns sentiment scores in real time
- Categorizes emotions:
  - 😊 Positive (compound ≥ 0.05)
  - 😐 Neutral (between −0.05 and 0.05)
  - 😞 Negative (compound ≤ −0.05)

### 🔹 HTML5, CSS3, JavaScript (Frontend UI)
Used to build a clean, user-friendly chat interface:
- JavaScript Fetch API for sending messages to Flask backend
- Dynamic real-time message rendering
- Sentiment display beside each user message

### 🔹 Sessions for Conversation Memory
Flask session is used to store the full chat and sentiment history for each user in the browser session.

### 🔹 PyTest (Optional Testing)
Provides automated unit testing for validating sentiment classification correctness.

---

## 🎯 Key Capabilities

| Feature | Description |
|--------|-------------|
| Real-time chat | Users chat with a bot through a web browser |
| Sentiment per message | Displays mood for every user message |
| Overall mood evaluation | Computes average emotional score |
| Mood trend analysis | Detects whether mood improves or worsens |
| Session-based chat history | Maintains full conversation context |
| Emotion-aware bot responses | Replies vary based on user sentiment |
| Reset option | Allows starting a fresh conversation |

---

## 🚀 How to Run the Project

### 1️⃣ Install Python (if not installed)
Download from: https://www.python.org/

---

After installing download all the necessary libraries as pip install...


Then run the app.py file 

