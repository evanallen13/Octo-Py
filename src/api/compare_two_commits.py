import requests

def compare_commits(token, owner, repo, base_commit, head_commit):
    """Compare two commits and return the changes between them."""
    url = f"https://api.github.com/repos/{owner}/{repo}/compare/{base_commit}...{head_commit}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # Returns details of changed files, commits, etc.
    else:
        return {"error": response.status_code, "message": response.json()}
