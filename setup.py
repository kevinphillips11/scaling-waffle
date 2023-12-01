# setup.py

import subprocess
import os
import time

def checkout_repository():
    subprocess.run(['git', 'clone', os.getenv('GITHUB_REPOSITORY')])

def set_up_python():
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

def install_ngrok():
    subprocess.run(['sudo', 'snap', 'install', 'ngrok'])

def authenticate_ngrok(ngrok_token):
    subprocess.run(['ngrok', 'authtoken', ngrok_token])

def start_ngrok():
    subprocess.Popen(['ngrok', 'http', '--domain=handy-labrador-humane.ngrok-free.app', '5000'])

def run_app_forever():
    subprocess.Popen(['nohup', 'python', 'app.py'])

def sleep_forever():
    time.sleep(float('inf'))

if __name__ == '__main__':
    ngrok_token = os.getenv('NGROK_TOKEN')

    checkout_repository()
    set_up_python()
    install_ngrok()
    
    authenticate_ngrok(ngrok_token)
    start_ngrok()
    run_app_forever()
    sleep_forever()
