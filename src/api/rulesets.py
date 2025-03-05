import requests

class Rulesets:
    def __init__(self, token: str, org: str = None, repo: str = None):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
        self.org = org
        self.repo = repo

    ## Ruleset Management for Organizations ##

    def list_org_rulesets(self):
        """List all rulesets for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/rulesets"
        return requests.get(url, headers=self.headers).json()

    def get_org_ruleset(self, ruleset_id: int):
        """Get a specific ruleset for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/rulesets/{ruleset_id}"
        return requests.get(url, headers=self.headers).json()

    def create_org_ruleset(self, ruleset_data: dict):
        """Create a new ruleset for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/rulesets"
        return requests.post(url, json=ruleset_data, headers=self.headers).json()

    def update_org_ruleset(self, ruleset_id: int, ruleset_data: dict):
        """Update an existing ruleset for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/rulesets/{ruleset_id}"
        return requests.put(url, json=ruleset_data, headers=self.headers).json()

    def delete_org_ruleset(self, ruleset_id: int):
        """Delete a ruleset from an organization."""
        url = f"{self.base_url}/orgs/{self.org}/rulesets/{ruleset_id}"
        return requests.delete(url, headers=self.headers).json()

    ## Ruleset Management for Repositories ##

    def list_repo_rulesets(self):
        """List all rulesets for a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/rulesets"
        return requests.get(url, headers=self.headers).json()

    def get_repo_ruleset(self, ruleset_id: int):
        """Get a specific ruleset for a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/rulesets/{ruleset_id}"
        return requests.get(url, headers=self.headers).json()

    def create_repo_ruleset(self, ruleset_data: dict):
        """Create a new ruleset for a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/rulesets"
        return requests.post(url, json=ruleset_data, headers=self.headers).json()

    def update_repo_ruleset(self, ruleset_id: int, ruleset_data: dict):
        """Update an existing ruleset for a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/rulesets/{ruleset_id}"
        return requests.put(url, json=ruleset_data, headers=self.headers).json()

    def delete_repo_ruleset(self, ruleset_id: int):
        """Delete a ruleset from a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/rulesets/{ruleset_id}"
        return requests.delete(url, headers=self.headers).json()
