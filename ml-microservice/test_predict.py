
import requests

url = "http://127.0.0.1:8000/predict"
sample_data = {"message": "You’ve won a free iPhone! Click here to claim."}

response = requests.post(url, json=sample_data)

print("Status Code:", response.status_code)
print("Response:", response.json())
