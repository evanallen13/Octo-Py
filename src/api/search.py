import requests

class Search:
    def __init__(self, token: str):
        self.base_url = "https://api.github.com/search"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }

    def search_repositories(self, query: str, sort: str = "stars", order: str = "desc"):
        """Search for repositories based on a query."""
        url = f"{self.base_url}/repositories?q={query}&sort={sort}&order={order}"
        return requests.get(url, headers=self.headers).json()

    def search_code(self, query: str):
        """Search for code snippets in public repositories."""
        url = f"{self.base_url}/code?q={query}"
        return requests.get(url, headers=self.headers).json()

    def search_issues(self, query: str, sort: str = "created", order: str = "desc"):
        """Search for issues and pull requests."""
        url = f"{self.base_url}/issues?q={query}&sort={sort}&order={order}"
        return requests.get(url, headers=self.headers).json()

    def search_commits(self, query: str):
        """Search for commits across repositories."""
        url = f"{self.base_url}/commits?q={query}"
        return requests.get(url, headers=self.headers).json()

    def search_users(self, query: str):
        """Search for GitHub users."""
        url = f"{self.base_url}/users?q={query}"
        return requests.get(url, headers=self.headers).json()
