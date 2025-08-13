# source env/Scripts/activate
# Install a package eg: pip install requests

import requests

response = requests.get('https://pypi.org/pypi')
print(response)
