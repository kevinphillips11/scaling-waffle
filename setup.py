# setup.py

import subprocess
import os
import time
import sys

def checkout_repository():
    repo_url = os.getenv('GITHUB_REPOSITORY')
    print(f"Repository URL: {repo_url}")
    subprocess.run(['git', 'clone', repo_url])

def set_up_python():
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

def install_ngrok():
    subprocess.run(['sudo', 'snap', 'install', 'ngrok'])

def authenticate_ngrok(ngrok_token):
    # Set NGROK_HOME to a directory where the runner has write permissions
    os.environ['NGROK_HOME'] = '/home/runner/ngrok_home'
    subprocess.run(['ngrok', 'authtoken', ngrok_token])

def start_ngrok():
    subprocess.Popen(['ngrok', 'http', '--domain=handy-labrador-humane.ngrok-free.app', '5000'])

def run_app_forever():
    subprocess.Popen(['nohup', 'python', 'app.py'])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python setup.py <ngrok_token>")
        sys.exit(1)

    ngrok_token = sys.argv[1]

    checkout_repository()
    set_up_python()
    install_ngrok()
    
    authenticate_ngrok(ngrok_token)
    start_ngrok()
    run_app_forever()

    while True:
        time.sleep(1)
