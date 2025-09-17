import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()  # loads variables from the .env file into environment
GUARDIAN_API_KEY = os.getenv("GUARDIAN_API_KEY")


def fetch_news_for_period(query, from_date, to_date, page_size=10):
    url = "https://content.guardianapis.com/search"
    params = {
        "q": query,
        "from-date": from_date,
        "to-date": to_date,
        "section": "politics",  # politics section for relevance
        "order-by": "newest",
        "show-fields": "headline,byline,short-url,bodyText",
        "page-size": page_size,
        "api-key": GUARDIAN_API_KEY,
        "lang": "en"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    results = data.get("response", {}).get("results", [])
    articles = []
    for article in results:
        fields = article.get("fields", {})
        headline = fields.get("headline", "")
        byline = fields.get("byline", "")
        url = article.get("webUrl", "")
        snippet = fields.get("bodyText", "")[:300].replace('\n', ' ')
        articles.append(f"{headline} by {byline}\nSnippet: {snippet}\nRead more: {url}")
    return articles


def fetch_news_by_month(query, start_date, end_date, articles_per_month=10):
    current_date = start_date
    all_articles = {}
    while current_date < end_date:
        next_month = (current_date + timedelta(days=32)).replace(day=1)
        from_date_str = current_date.strftime("%Y-%m-%d")
        to_date_str = (next_month - timedelta(days=1)).strftime("%Y-%m-%d")
        print(f"Fetching articles from {from_date_str} to {to_date_str}...")

        articles = fetch_news_for_period(query, from_date_str, to_date_str, page_size=articles_per_month)
        all_articles[from_date_str[:-3]] = articles  # store by year-month e.g. "2024-07"

        current_date = next_month

    return all_articles


if __name__ == "__main__":
    query = '"Labour Party" OR "Labour Party UK" OR Labour'
    start_date = datetime(2024, 7, 1)
    end_date = datetime(2025, 7, 1)

    monthly_articles = fetch_news_by_month(query, start_date, end_date, articles_per_month=10)

    for month, articles in monthly_articles.items():
        print(f"\nMonth: {month} | Articles fetched: {len(articles)}")
        print("-" * 60)
        for article in articles:
            print(article)
            print()
        print("=" * 80)