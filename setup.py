# setup.py

import subprocess
import os
import sys
import time

def checkout_repository(repo_url):
    subprocess.run(['git', 'clone', repo_url])

def set_up_python():
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

def install_ngrok():
    subprocess.run([
        'curl', '-s', 'https://ngrok-agent.s3.amazonaws.com/ngrok.asc', '|',
        'sudo', 'tee', '/etc/apt/trusted.gpg.d/ngrok.asc', '>/dev/null'
    ])
    subprocess.run([
        'echo', '"deb https://ngrok-agent.s3.amazonaws.com buster main"',
        '|', 'sudo', 'tee', '/etc/apt/sources.list.d/ngrok.list'
    ])
    subprocess.run(['sudo', 'apt', 'update'])
    subprocess.run(['sudo', 'apt', 'install', 'ngrok'])

def authenticate_ngrok(ngrok_token):
    subprocess.run(['ngrok', 'config', 'add-authtoken', ngrok_token])

def start_ngrok():
    subprocess.Popen(['ngrok', 'http', '--domain=handy-labrador-humane.ngrok-free.app', '5000'])

def run_app_forever():
    subprocess.Popen(['nohup', 'python', 'app.py'])

def sleep_forever():
    time.sleep(float('inf'))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python setup.py <repository_url> <ngrok_token>")
        sys.exit(1)

    repo_url = sys.argv[1]
    ngrok_token = sys.argv[2]

    checkout_repository(repo_url)
    set_up_python()
    install_ngrok()
    
    authenticate_ngrok(ngrok_token)
    start_ngrok()
    run_app_forever()
    sleep_forever()
