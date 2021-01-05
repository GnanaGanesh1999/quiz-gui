import requests

URL = "https://opentdb.com/api.php?amount=10&type=boolean"
response = requests.get(url=URL)
question_data = response.json()["results"]
