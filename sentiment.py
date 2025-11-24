# sentiment.py
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure VADER lexicon is available (only runs once on first import)
try:
    _ = SentimentIntensityAnalyzer()
except LookupError:
    nltk.download("vader_lexicon")
    
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text: str) -> dict:
    """
    Return VADER scores + simple label.
    """
    scores = sia.polarity_scores(text)
    compound = scores["compound"]
    if compound >= 0.05:
        label = "Positive"
    elif compound <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "label": label,
        "compound": compound,
        "scores": scores
    }


def overall_conversation_sentiment(user_messages: list[str]) -> dict:
    """
    Compute overall sentiment for the conversation (only user messages).
    """
    if not user_messages:
        return {
            "label": "Neutral",
            "average_compound": 0.0,
            "trend": "No messages yet."
        }

    scores = [analyze_sentiment(m)["compound"] for m in user_messages]
    avg = sum(scores) / len(scores)

    if avg >= 0.05:
        label = "Positive"
    elif avg <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    # Simple trend (Tier 2 enhancement)
    first = scores[0]
    last = scores[-1]
    if last - first > 0.1:
        trend = "Mood improved over the conversation."
    elif last - first < -0.1:
        trend = "Mood worsened over the conversation."
    else:
        trend = "Mood stayed relatively stable."

    return {
        "label": label,
        "average_compound": avg,
        "trend": trend
    }
