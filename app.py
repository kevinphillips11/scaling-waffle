from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from lastmileai import LastMile
import signal
import time

lastmile = LastMile(api_key=os.environ["LASTMILEAI_API_KEY"])

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = "b5b9a807cf6649128b07b112213b234d"  # Replace with your News API key

# Flag to track whether the server should be shut down
shutdown_flag = False

def shutdown_server():
    print('Shutting down...')
    os.kill(os.getpid(), signal.SIGINT)

@app.route('/close_the_app')
def close_the_app():
    token = request.args.get('token')
    if token == 'johnlocke':
        global shutdown_flag
        shutdown_flag = True
        return 'Server will shut down after processing current requests...'
    else:
        return 'Invalid token'

@app.route('/v1/chat/completions', methods=['POST'])
def chat_completions():
    if shutdown_flag:
        shutdown_server()
    data = request.get_json()
    messages = data['messages']
    completion = lastmile.create_openai_chat_completion(
      completion_params = {
        'model': "gpt-4",
        'messages': messages,
      }
    )
    return completion["completionResponse"]["choices"][0]["message"]["content"]

@app.route('/')
def index():
    # Fetch top headlines from News API
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()

    # Extract relevant information from the response
    articles = news_data.get('articles', [])

    if shutdown_flag:
        shutdown_server()

    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)

    # Allow the server to run for 5 minutes
    start_time = time.time()
    while time.time() - start_time < 300 and not shutdown_flag:
        time.sleep(1)

    # After 5 minutes or if the shutdown flag is set, shut down the server
    if not shutdown_flag:
        shutdown_server()
