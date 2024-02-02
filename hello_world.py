import requests

url = (
    "https://jvzwetgvna.execute-api.us-west-1.amazonaws.com/default/HelloWorldFunction"
)

data = {"number1": 1, "number2": 2}

response = requests.post(url, json=data)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
