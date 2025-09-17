from datetime import datetime
from fetch_news import fetch_news_by_month
from topic_modeling import topic_modeling
from llama_sentiment_analysis import llama_sentiment_classify
from visualize_sentiments import visualize_sentiments

def main():
    query = '"Labour Party" OR "Labour Party UK" OR Labour'
    start_date = datetime(2024, 7, 1)
    end_date = datetime(2025, 7, 1)

    print("Fetching Labour Party news month-by-month...")
    monthly_articles = fetch_news_by_month(query, start_date, end_date, articles_per_month=10)

    monthly_sentiments = {}
    for month, articles in monthly_articles.items():
        print(f"Classifying sentiment for {month} with {len(articles)} articles...")
        # If articles are strings (full text)
        texts = [article[:1000] for article in articles]
        sentiments = llama_sentiment_classify(texts)
        monthly_sentiments[month] = sentiments

    print("Visualizing sentiment trends...")
    visualize_sentiments(monthly_sentiments)

if __name__ == "__main__":
    main()