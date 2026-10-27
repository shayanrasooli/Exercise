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
    "X-Student-ID": "student_Shayan_r"
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