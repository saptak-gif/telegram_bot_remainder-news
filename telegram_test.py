import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = "Testing from GitHub Actions"

url = f"https://api.telegram.org/bot{8565676723:AAEKEI3w9oakwnMiw6kE6U2wbWqVxHs6S5I}/sendMessage"

r = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)

print(r.text)
