import ollama

model = 'llama3.2:latest'
def llama_sentiment_classify(texts):
    results = []
    for text in texts:
        try:
            response = ollama.chat(
                model=model,
                messages=[
                    {"role": "system", "content": "You are an assistant that classifies the sentiment of news articles as Positive, Negative, or Neutral."},
                    {"role": "user", "content": f"Classify the sentiment as Positive, Negative, or Neutral:\n\n{text}"}
                ],
                stream=False,
            )
            content = response['message']['content'].strip()
            if "positive" in content.lower():
                sentiment = "Positive"
            elif "negative" in content.lower():
                sentiment = "Negative"
            elif "neutral" in content.lower():
                sentiment = "Neutral"
            else:
                sentiment = "Neutral"  # default fallback
            results.append(sentiment)
        except Exception as e:
            print(f"An error occurred with llama: {e}")
            results.append("Neutral")  # safe fallback
    return results

if __name__ == "__main__":
    example_texts = [
        "Stocks rallied today as tech companies reported strong earnings...",
        "Automaker recalls vehicles citing safety concerns related to brakes..."
    ]
    summaries = llama_summarize(example_texts)
    for summary in summaries:
        print(summary)