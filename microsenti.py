# sentiment_analysis_service.py

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, request, jsonify

nltk.download('vader_lexicon')

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    text = request.json['text']
    sentiment_score = sia.polarity_scores(text)['compound']
    return jsonify({'sentiment': sentiment_score})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
