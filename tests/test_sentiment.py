# tests/test_sentiment.py
from sentiment import analyze_sentiment, overall_conversation_sentiment

def test_analyze_sentiment_positive():
    result = analyze_sentiment("I love this service, it's fantastic!")
    assert result["label"] == "Positive"

def test_analyze_sentiment_negative():
    result = analyze_sentiment("This is terrible and I hate it.")
    assert result["label"] == "Negative"

def test_overall_conversation():
    msgs = [
        "This is bad.",
        "I am unhappy.",
        "Not satisfied at all."
    ]
    result = overall_conversation_sentiment(msgs)
    assert result["label"] == "Negative"
