import requests
import json

url = "http://localhost:8000/api/create/"
data = {
    "title": "Finish Homework",
    "body": "Complete the Python exercises"
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())

