# Request for getting data from server
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("URL")
ENDPOINT = "/stage/1"

URL = f"{BASE_URL.rstrip("/")}/{ENDPOINT.lstrip("/")}"
print (URL)

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
print(type(response))
print(type(response.json()))
print(type(response.text))


try:
    print(response.json())
except ValueError:
    print(response.text)

except requests.exceptions.RequestException as error:
    print("Request failed:", error)

data = response.json()
clues = data["clues"]

for i in range (len(data["agents"])):
    if data["agents"][i]["code"].startswith(clues["code_prefix"]) and data["agents"][i]["active"] == clues["active_only"]:
        target = data["agents"][i]["name"]
        print(f"target is {target}")
        print (i)
        break

POST_ENDPOINT = "/stage/1/submit"

POST_URL = f"{BASE_URL.rstrip("/")}/{POST_ENDPOINT.lstrip("/")}"

BODY = {
    "name":target
}


submit_response = requests.post(
    POST_URL,
    headers=HEADER,
    json=BODY
)

print("Status Code:", submit_response.status_code)
print(submit_response.text)

