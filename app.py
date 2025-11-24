# app.py
from flask import Flask, render_template, request, jsonify, session
from sentiment import analyze_sentiment, overall_conversation_sentiment
from chatbot import generate_bot_reply
from uuid import uuid4

app = Flask(__name__)
app.secret_key = "replace-with-a-random-secret-key"  # IMPORTANT for sessions


def get_session_id():
    if "session_id" not in session:
        session["session_id"] = str(uuid4())
        session["conversation"] = []  # list of dicts: {sender, text, sentiment}
    return session["session_id"]


def get_conversation():
    if "conversation" not in session:
        session["conversation"] = []
    return session["conversation"]


def save_conversation(conv):
    session["conversation"] = conv


@app.route("/")
def index():
    get_session_id()  # ensure session initialized
    return render_template("index.html")


@app.route("/api/message", methods=["POST"])
def api_message():
    get_session_id()
    conversation = get_conversation()

    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Statement-level sentiment for this message (Tier 2)
    user_sentiment = analyze_sentiment(user_message)

    # Store user message
    conversation.append({
        "sender": "user",
        "text": user_message,
        "sentiment": user_sentiment["label"],
        "compound": user_sentiment["compound"]
    })

    # Bot reply
    bot_reply = generate_bot_reply(user_message)
    conversation.append({
        "sender": "bot",
        "text": bot_reply
    })

    save_conversation(conversation)

    # Return latest message + full conversation
    return jsonify({
        "bot_reply": bot_reply,
        "user_sentiment": user_sentiment,
        "conversation": conversation
    })


@app.route("/api/summary", methods=["GET"])
def api_summary():
    get_session_id()
    conversation = get_conversation()

    user_messages = [m["text"] for m in conversation if m["sender"] == "user"]
    summary = overall_conversation_sentiment(user_messages)

    return jsonify({
        "overall_label": summary["label"],
        "average_compound": summary["average_compound"],
        "trend": summary["trend"],
        "user_message_count": len(user_messages)
    })


@app.route("/api/reset", methods=["POST"])
def api_reset():
    """
    Clears the conversation for a fresh start.
    """
    session["conversation"] = []
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
