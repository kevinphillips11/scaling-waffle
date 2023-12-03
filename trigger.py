import requests
import os

def trigger_workflow(username, repo_name, workflow_id, token, artist_name):
    api_url = f"https://api.github.com/repos/{username}/{repo_name}/actions/workflows/{workflow_id}/dispatches"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    
    payload = {
        "ref": "main",
        # "inputs": {
        #     "artist_name": artist_name,
        # }
    }
    
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 204:
        print("Workflow triggered successfully.")
    else:
        print(f"Failed to trigger workflow. Status code: {response.status_code}")
        print(response.text)

# Replace these values with your actual GitHub information
username = "kevinphillips11"
repo_name = "scaling-waffle"
workflow_id = "news.yml"
token = os.environ['PAT_TOKEN']
artist_name = "john frusciante"

trigger_workflow(username, repo_name, workflow_id, token, artist_name)
