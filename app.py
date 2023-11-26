from flask import Flask, render_template
from flask_cors import CORS
import requests
import os
from lastmileai import LastMile

lastmile = LastMile(api_key=os.environ["LASTMILEAI_API_KEY"])

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = "b5b9a807cf6649128b07b112213b234d"  # Replace with your News API key

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    data = request.get_json()
    messages = data['messages']
    completion = lastmile.create_openai_chat_completion(
      completion_params = {
        model: "gpt-4",
        messages: messages,
      }
    )
    return completion

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
