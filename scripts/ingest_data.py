import yfinance as yf
import pandas as pd
from newsapi import NewsApiClient
from textblob import TextBlob
from datetime import datetime
import os

# 1. SETUP - Get a free key from newsapi.org
NEWS_API_KEY = 'YOUR_NEWS_API_KEY' 
newsapi = NewsApiClient(api_key='c27e59821bd04200a40cc5774e191bbf')

def get_market_data(ticker="AAPL"):
    print(f"Fetching market data for {ticker}...")
    stock = yf.Ticker(ticker)
    df = stock.history(period="1d", interval="1m") # 1-minute intervals
    df['ticker'] = ticker
    return df

def get_sentiment_data(query="Apple"):
    print(f"Fetching news for {query}...")
    # Fetch headlines from the last 24 hours
    articles = newsapi.get_everything(q=query, language='en', sort_by='relevancy')
    
    data = []
    for art in articles['articles'][:10]: # Top 10 headlines
        analysis = TextBlob(art['title'])
        data.append({
            'timestamp': art['publishedAt'],
            'headline': art['title'],
            'sentiment': analysis.sentiment.polarity # -1 (Neg) to 1 (Pos)
        })
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Fetch
    prices = get_market_data("AAPL")
    news = get_sentiment_data("Apple Inc")

    # Ensure the data/raw directory exists
    os.makedirs("data/raw", exist_ok=True)

    # Save to 'data/raw' folder
    prices.to_csv("data/raw/raw_prices.csv")
    news.to_csv("data/raw/raw_sentiment.csv")
    print("Success! Files saved in data/raw/ folder.")