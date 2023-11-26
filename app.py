from flask import Flask, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = "b5b9a807cf6649128b07b112213b234d"  # Replace with your News API key

@app.route('/')
def index():
    # Fetch top headlines from News API
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()

    # Extract relevant information from the response
    articles = news_data.get('articles', [])

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
