import pandas as pd
import re
import nltk
import warnings
from nltk.corpus import stopwords


warnings.filterwarnings("ignore")


nltk.download('stopwords', quiet=True)
STOPWORDS = set(stopwords.words('english'))

def clean_text(text):
   
    if not isinstance(text, str):
        return ""
    
    text = re.sub(r'http\S+|www.\S+', '', text)  # remove URLs
    text = re.sub(r'@\w+', '', text)             # remove mentions
    text = re.sub(r'#', '', text)                # remove hashtags
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # remove punctuation
    text = text.lower().strip()                  # lowercase and remove extra spaces
    tokens = [t for t in text.split() if t not in STOPWORDS]  # remove stopwords
    return ' '.join(tokens)

def load_and_clean(csv_path, text_col='tweet'):
  
    df = pd.read_csv(csv_path)
    df['clean_text'] = df[text_col].astype(str).apply(clean_text)
    return df

if __name__ == '__main__':
    # Auto paths
    input_csv = "data/raw/tesla_tweets.csv"
    output_csv = "data/processed/cleaned.csv"

    df = load_and_clean(input_csv)
    df.to_csv(output_csv, index=False)
    print(f"✅ Saved cleaned CSV to {output_csv}")
