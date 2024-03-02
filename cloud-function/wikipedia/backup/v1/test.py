import requests

# Replace with your cloud function URL
URL = "http://localhost:8080/cloud-function"

# Replace with your desired object of interest
object_of_interest = "Artificial Intelligence"

# Build the payload
payload = {"object_of_interest": object_of_interest}

# Send the POST request
response = requests.post(URL, json=payload)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    summary = data.get("summary")
    print(f"Wikipedia summary for '{object_of_interest}':\n{summary}")
else:
    print(f"Error: {response.status_code} - {response.text}")