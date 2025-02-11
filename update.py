import requests
import json

url = "http://localhost:8000/api/update/1/"  # Update Todo with id 1
data = {
    "title": "Finish Homework - Updated",
    "body": "Complete the Python exercises and review concepts"
}

headers = {'Content-Type': 'application/json'}

response = requests.put(url, headers=headers, data=json.dumps(data))

#print(response.json())


url = "http://localhost:8000/api/delete/6"  # Delete Todo with id 1

response = requests.delete(url)

print(response)

