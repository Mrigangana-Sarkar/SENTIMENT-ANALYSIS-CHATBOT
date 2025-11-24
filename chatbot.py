# chatbot.py
from sentiment import analyze_sentiment

def generate_bot_reply(user_message: str) -> str:
    """
    Very simple rule-based bot that reacts to sentiment.
    You can make this as fancy as you like.
    """
    sent = analyze_sentiment(user_message)
    label = sent["label"]

    if label == "Negative":
        return (
            "I’m sorry you feel that way. "
            "Could you tell me more so I can try to help?"
        )
    elif label == "Positive":
        return (
            "Glad to hear that! 😊 "
            "Is there anything else you’d like to talk about?"
        )
    else:
        return (
            "I understand. "
            "Tell me more about what’s on your mind."
        )
