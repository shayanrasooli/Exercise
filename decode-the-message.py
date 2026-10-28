import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("URL")
ENDPOINT = "/stage/2"

URL = f"{BASE_URL.rstrip("/")}/{ENDPOINT.lstrip("/")}"


HEADER = {
    "X-Student-ID": "student_shayan-r"
}


response = requests.get(
    URL,
    headers=HEADER,
    timeout=30
)

print("Status Code:", response.status_code)
print("Response:")

try:
    print(response.json())
except ValueError:
    print(response.text)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)


data = response.json()

print (len(data["messages"]))
print (data["messages"][1])

for message in data["messages"]:
    if "TRANSMISSION-VALID" in message:
        print(message)
        value = message.split("KEY=",1)[1][:5]
        break

POST_ENDPOINT = "/stage/2/submit"

POST_URL = f"{BASE_URL.rstrip("/")}/{POST_ENDPOINT.lstrip("/")}"

BODY = {
    "keyword":value
}


submit_response = requests.post(
    POST_URL,
    headers=HEADER,
    json=BODY
)

print("Status Code:", submit_response.status_code)
print(submit_response.text)

