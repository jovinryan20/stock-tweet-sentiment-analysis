import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load CSV
df = pd.read_csv("data/processed/cleaned.csv")  # use your clean CSV

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment scores
def get_sentiment(text):
    scores = analyzer.polarity_scores(str(text))
    return pd.Series([scores['neg'], scores['neu'], scores['pos'], scores['compound']])

# Apply to the 'clean_text' column
df[['neg', 'neu', 'pos', 'compound']] = df['clean_text'].apply(get_sentiment)

# Optional: categorize sentiment based on compound score
def sentiment_label(compound):
    if compound >= 0.05:
        return 'Positive'
    elif compound <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['compound'].apply(sentiment_label)

# Save the sentiment-analyzed CSV
df.to_csv("data/cleaned_sentiment.csv", index=False)
print("✅ Saved CSV with sentiment scores to data/processed/cleaned_sentiment.csv")
