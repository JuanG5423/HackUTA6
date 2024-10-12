from transformers import pipeline

# Load sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze sentiment of a text
result = sentiment_analyzer("I'm feeling fantastic today!")
print(result)  # Output: [{'label': 'POSITIVE', 'score': 0.9998}]

# For emotion detection
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
emotions = emotion_analyzer("I feel so stressed and anxious about my work.")
print(emotions)
