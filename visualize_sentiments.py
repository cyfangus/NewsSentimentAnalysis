import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def visualize_sentiments(monthly_sentiments):
    months = sorted(monthly_sentiments.keys())
    pos_counts, neg_counts, neu_counts = [], [], []

    for month in months:
        sentiments = monthly_sentiments[month]
        pos_counts.append(sentiments.count('Positive'))
        neg_counts.append(sentiments.count('Negative'))
        neu_counts.append(sentiments.count('Neutral'))

    plt.figure(figsize=(12, 6))
    plt.plot(months, pos_counts, label='Positive', marker='o')
    plt.plot(months, neg_counts, label='Negative', marker='o')
    plt.plot(months, neu_counts, label='Neutral', marker='o')
    plt.xticks(rotation=45)
    plt.xlabel("Month")
    plt.ylabel("Number of Articles")
    plt.title("Monthly Sentiment Trend on Labour Party News in The Guardian")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example mock data for testing
    sample_data = {
        "2024-07": ["Positive", "Positive", "Neutral", "Negative", "Positive", "Neutral", "Negative", "Neutral", "Positive", "Positive"],
        "2024-08": ["Negative", "Negative", "Neutral", "Negative", "Positive", "Neutral", "Negative", "Neutral", "Negative", "Positive"],
        "2024-09": ["Neutral", "Neutral", "Neutral", "Neutral", "Positive", "Neutral", "Neutral", "Neutral", "Neutral", "Neutral"],
        "2024-10": ["Positive", "Positive", "Positive", "Positive", "Positive", "Positive", "Positive", "Positive", "Positive", "Positive"],
        "2024-11": ["Negative", "Negative", "Negative", "Negative", "Negative", "Negative", "Negative", "Negative", "Negative", "Negative"],
    }

    visualize_sentiments(sample_data)