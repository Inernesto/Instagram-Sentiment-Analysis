from google.cloud import language_v1
from datetime import date

# Initialize the Google Natural Language API client
client = language_v1.LanguageServiceClient()


def analyze_sentiments(comments):
    # Initialize variables to calculate average sentiment
    total_score = 0
    total_magnitude = 0
    sentiment_scores = []

    for comment in comments:
        # Analyze sentiment using Google Natural Language API
        response = client.analyze_sentiment(
            document=language_v1.Document(content=comment, type_=language_v1.Document.Type.PLAIN_TEXT))

        sentiment = response.document_sentiment
        score = sentiment.score
        magnitude = sentiment.magnitude

        # Append the scores and magnitude to the list
        sentiment_scores.append({"score": score, "magnitude": magnitude})

        # Calculate running totals
        total_score += score
        total_magnitude += magnitude

    # Calculate the average sentiment score and magnitude
    if len(comments) > 0:
        average_score = total_score / len(comments)
        average_magnitude = total_magnitude / len(comments)
    else:
        average_score = 0
        average_magnitude = 0

    return {
        "average_score": average_score,
        "average_magnitude": average_magnitude,
        "sentiment_scores": sentiment_scores,
        "date": int(date.today().strftime("%Y%m%d"))
    }
