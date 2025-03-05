import os
from OctoPy import OctoPy

token = os.getenv('GITHUB_TOKEN')
org = os.getenv('GITHUB_ORG')
enterprise = os.getenv('GITHUB_ENTERPRISE')

octopy = OctoPy(token, org, enterprise)

rulesets = octopy.list_org_rulesets()

for ruleset in rulesets:
    print(ruleset)