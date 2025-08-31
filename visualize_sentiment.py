import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sentiment CSV
df = pd.read_csv("data/processed/cleaned_sentiment.csv")

# Dark Theme Setup (optional)

sns.set_theme(style="darkgrid", palette="bright")  # Seaborn darkgrid
plt.rcParams.update({
    'axes.facecolor': '#111111',    # Plot background
    'figure.facecolor': '#111111',  # Figure background
    'axes.edgecolor': 'white',      # Axis lines
    'axes.labelcolor': 'white',     # Axis labels
    'xtick.color': 'white',         # X ticks
    'ytick.color': 'white',         # Y ticks
    'text.color': 'white',          # Text color
    'grid.color': 'gray'            # Grid lines
})

# Countplot
plt.figure(figsize=(6,4))
sns.countplot(x='sentiment', data=df, order=['Positive','Neutral','Negative'])
plt.title('Tweet Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Tweets')
plt.savefig("plots/sentiment_distribution.png", dpi=300, bbox_inches='tight')
plt.show()

# Histogram of Compound Scores
plt.figure(figsize=(6,4))
sns.histplot(df['compound'], bins=30, kde=True, color='cyan')
plt.title('Distribution of Compound Sentiment Scores')
plt.xlabel('Compound Score')
plt.ylabel('Frequency')
plt.savefig("plots/compound_scores.png", dpi=300, bbox_inches='tight')
plt.show()

# Average Sentiment Over Time
df['date'] = pd.to_datetime(df['date'], errors='coerce')
daily_sentiment = df.groupby('date')['compound'].mean().reset_index()

plt.figure(figsize=(10,5))
sns.lineplot(x='date', y='compound', data=daily_sentiment, marker='o', color='lime')
plt.title('Average Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Average Compound Score')
plt.xticks(rotation=45)
plt.savefig("plots/average_sentiment_over_time.png", dpi=300, bbox_inches='tight')
plt.show()
