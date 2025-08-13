import requests
from mamadpdf import pdf2text

# ? first run pipenv shell to activate the virtual environment
# ? then run python app.py to run the application
# ? by using exit we can deactivate the virtual environment

response = requests.get('https://pypi.org/pypi/pipenv/json')
# data = response.json()
# print(data)
print(response.status_code)

pdf2text.convertToText()
