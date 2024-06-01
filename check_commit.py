import requests
import subprocess

GITHUB_API_URL = 'https://api.github.com'
REPO_OWNER = 'muzahidulnisar'
REPO_NAME = 'animated-navigation-html'
BRANCH_NAME = 'main'
LAST_COMMIT_FILE = '/home/ubuntu/last_commit.txt'
LATEST_DEPLOY_SCRIPT = '/home/ubuntu/latest_code_deploy.sh'

def get_latest_commit_sha():
    try:
        url = f'{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/commits/{BRANCH_NAME}'
        response = requests.get(url)
        return response.json()['sha']
    except Exception as e:
        print(e)

def read_last_commit_sha():
    try:
        with open(LAST_COMMIT_FILE, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def write_last_commit_sha(sha):
    with open(LAST_COMMIT_FILE, 'w') as file:
        file.write(sha)

def main():
    latest_sha = get_latest_commit_sha()
    previous_sha = read_last_commit_sha()

    if latest_sha != previous_sha:
        print('New commit found!')
        write_last_commit_sha(latest_sha)
        subprocess.run(['sudo', 'bash', LATEST_DEPLOY_SCRIPT])
    else:
        print('No New commit found!')

if __name__ == '__main__':
    main()