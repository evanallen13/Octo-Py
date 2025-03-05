import json
import os
from github import Auth
from github import GithubIntegration
# From src
from src.api.copilot import Copilot
from src.api.rulesets import Rulesets
from src.api.custom_properties import CustomProperties

class OctoPy(Copilot, Rulesets, CustomProperties):
    def __init__(self, 
                token: str, 
                org: str, 
                enterprise: str = None,
                app_id: str = None):
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
        self.org = org
        self.enterprise = enterprise
        
        if token is None and app_id is not None:
            token = self.create_token()
            
        self.token = token
        
    def create_token(self):
        app_id = '1076799'
        key_path = os.path.normpath(os.path.expanduser('./app_key.pem'))

        with open(key_path, 'r') as cert_file:
            app_key = cert_file.read()

        auth = Auth.AppAuth(app_id, app_key)
        gi = GithubIntegration(app_id, app_key)
        installations = gi.get_installations()

        installation_id = installations[0].id
        token = gi.get_access_token(installation_id).token
        
        return token