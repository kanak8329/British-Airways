import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Step 1: Download required resources
nltk.download('vader_lexicon')

# Step 2: Load the data
df = pd.read_csv("ba_reviews.csv")

# Step 3: Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Step 4: Apply sentiment analysis
df['Sentiment_Score'] = df['Review'].apply(lambda x: sia.polarity_scores(x)['compound'])
df['Sentiment_Label'] = df['Sentiment_Score'].apply(
    lambda x: 'Positive' if x > 0.05 else 'Negative' if x < -0.05 else 'Neutral'
)

# Step 5: Save results
df.to_csv("ba_reviews_with_sentiment.csv", index=False)
print("✅ Sentiment analysis complete! Check ba_reviews_with_sentiment.csv")
