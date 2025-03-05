import requests

class Copilot:
    def __init__(self, token: str, org: str, enterprise: str = None):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
        self.org = org
        self.enterprise = enterprise

    ## Copilot Metrics ##
    
    def get_copilot_metrics_enterprise(self):
        """Get Copilot metrics for an enterprise."""
        url = f"{self.base_url}/enterprises/{self.enterprise}/copilot/metrics"
        return requests.get(url, headers=self.headers).json()

    def get_copilot_metrics_org(self):
        """Get Copilot metrics for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/copilot/metrics"
        return requests.get(url, headers=self.headers).json()

    def get_copilot_metrics_team(self, team_slug: str):
        """Get Copilot metrics for a team."""
        url = f"{self.base_url}/orgs/{self.org}/teams/{team_slug}/copilot/metrics"
        return requests.get(url, headers=self.headers).json()

    ## Copilot Usage Metrics ##
    
    def get_copilot_usage_enterprise(self):
        """Get Copilot usage summary for enterprise members."""
        url = f"{self.base_url}/enterprises/{self.enterprise}/copilot/usage"
        return requests.get(url, headers=self.headers).json()

    def get_copilot_usage_org(self):
        """Get Copilot usage summary for organization members."""
        url = f"{self.base_url}/orgs/{self.org}/copilot/usage"
        return requests.get(url, headers=self.headers).json()

    def get_copilot_usage_team(self, team_slug: str):
        """Get Copilot usage summary for a team."""
        url = f"{self.base_url}/orgs/{self.org}/teams/{team_slug}/copilot/usage"
        return requests.get(url, headers=self.headers).json()

    ## Copilot User Management ##
    
    def list_copilot_seats_org(self, per_page: int = 30, page: int = 1):
        """List all Copilot seat assignments for an organization with pagination."""
        url = f"{self.base_url}/orgs/{self.org}/copilot/seats"
        params = {"per_page": per_page, "page": page}
        return requests.get(url, headers=self.headers, params=params).json()

    def get_copilot_seat_user(self, username: str):
        """Get Copilot seat assignment details for a specific user."""
        url = f"{self.base_url}/orgs/{self.org}/copilot/seats/{username}"
        return requests.get(url, headers=self.headers).json()

    def add_users_to_copilot(self, usernames: list):
        """Add users to the Copilot subscription for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/copilot/seats"
        data = {"users": usernames}
        return requests.post(url, json=data, headers=self.headers).json()

    def remove_users_from_copilot(self, usernames: list):
        """Remove users from the Copilot subscription for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/copilot/seats"
        data = {"users": usernames}
        return requests.delete(url, json=data, headers=self.headers).json()

    def add_teams_to_copilot(self, team_slugs: list):
        """Add teams to the Copilot subscription for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/copilot/seats/teams"
        data = {"teams": team_slugs}
        return requests.post(url, json=data, headers=self.headers).json()

    def remove_teams_from_copilot(self, team_slugs: list):
        """Remove teams from the Copilot subscription for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/copilot/seats/teams"
        data = {"teams": team_slugs}
        return requests.delete(url, json=data, headers=self.headers).json()
