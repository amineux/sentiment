from wordcloud import WordCloud
import matplotlib.pyplot as plt

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    payload = {'text': text}
    
    # Send request to the backend API
    response = requests.post(backend_api_url + '/process', json=payload)
    if response.status_code != 200:
        return 'Error processing request'

    # Extract relevant data from the response
    data = response.json()
    sentiment_text = data['sentiment']

    # Send request to the sentiment analysis service
    response = requests.post(sentiment_analysis_url, json=payload)
    if response.status_code != 200:
        return 'Error processing request'

    # Extract sentiment score from the response
    data = response.json()
    sentiment_score = data['sentiment']

    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400).generate(text)

    # Save word cloud as an image
    wordcloud.to_file('static/wordcloud.png')
    
    
    """dont forget to change html element 
    <h3>Word Cloud Visualization:</h3>
<img src="{{ url_for('static', filename='wordcloud.png') }}" alt="Word Cloud">
    """
  

    return render_template('result.html', text=text, sentiment_text=sentiment_text, sentiment_score=sentiment_score)
