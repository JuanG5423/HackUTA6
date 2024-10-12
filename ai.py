from transformers import pipeline

# Load sentiment analysis model
#sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze sentiment of a text
#result = sentiment_analyzer("I'm feeling fantastic today!")
#print(result)  # Output: [{'label': 'POSITIVE', 'score': 0.9998}]


print("This is in branch Juan")

# For emotion detection
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
emotions = emotion_analyzer("My friend went to the beach and gotgot a tan. Good on them")
print(emotions)
