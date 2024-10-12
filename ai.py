from transformers import pipeline

# Load sentiment analysis model
#sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze sentiment of a text
#result = sentiment_analyzer("I'm feeling fantastic today!")
#print(result)  # Output: [{'label': 'POSITIVE', 'score': 0.9998}]


# For emotion detection
emotion_analyzer = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

#emotions is a list containing a dictionary in the format [{'label': 'emotion', 'score': float}]

text = input("Enter text to analyze: ")
while text:
    emotions = emotion_analyzer(text)
    print(f"Emotion: {emotions[0]['label']}, Confidence: {emotions[0]['score']*100:.1f}%")
    text = input("Enter text to analyze: ")

