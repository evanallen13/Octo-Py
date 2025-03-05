import requests

class CustomProperties:
    def __init__(self, token: str, org: str, repo: str = None):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
        self.org = org
        self.repo = repo

    ## Custom Properties for Organizations ##
    
    def list_org_custom_properties(self):
        """List all custom properties for an organization."""
        url = f"{self.base_url}/orgs/{self.org}/custom_properties"
        return requests.get(url, headers=self.headers).json()

    def get_org_custom_property(self, property_name: str):
        """Get details of a specific custom property in an organization."""
        url = f"{self.base_url}/orgs/{self.org}/custom_properties/{property_name}"
        return requests.get(url, headers=self.headers).json()

    def create_org_custom_property(self, property_name: str, property_data: dict):
        """Create a new custom property in an organization."""
        url = f"{self.base_url}/orgs/{self.org}/custom_properties/{property_name}"
        return requests.put(url, json=property_data, headers=self.headers).json()

    def update_org_custom_property(self, property_name: str, property_data: dict):
        """Update an existing custom property in an organization."""
        url = f"{self.base_url}/orgs/{self.org}/custom_properties/{property_name}"
        return requests.patch(url, json=property_data, headers=self.headers).json()

    def delete_org_custom_property(self, property_name: str):
        """Delete a custom property from an organization."""
        url = f"{self.base_url}/orgs/{self.org}/custom_properties/{property_name}"
        return requests.delete(url, headers=self.headers).json()

    ## Custom Properties for Repositories ##
    
    def list_repo_custom_properties(self):
        """List all custom properties for a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/custom_properties"
        return requests.get(url, headers=self.headers).json()

    def get_repo_custom_property(self, property_name: str):
        """Get details of a specific custom property in a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/custom_properties/{property_name}"
        return requests.get(url, headers=self.headers).json()

    def create_repo_custom_property(self, property_name: str, property_data: dict):
        """Create a new custom property in a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/custom_properties/{property_name}"
        return requests.put(url, json=property_data, headers=self.headers).json()

    def update_repo_custom_property(self, property_name: str, property_data: dict):
        """Update an existing custom property in a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/custom_properties/{property_name}"
        return requests.patch(url, json=property_data, headers=self.headers).json()

    def delete_repo_custom_property(self, property_name: str):
        """Delete a custom property from a repository."""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/custom_properties/{property_name}"
        return requests.delete(url, headers=self.headers).json()
