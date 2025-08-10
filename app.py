from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment = 'Happy :)'
        image='/static/images/happy.png'
    elif sentiment_score < 0:
        sentiment = 'Sad :('
        image='/static/images/sad.png'
    else:
        sentiment = 'Neutral'
        image='/static/images/neutral.png'

    return render_template('result.html', text=text, sentiment=sentiment,image=image)

if __name__ == '__main__':
    app.run(debug=True)
