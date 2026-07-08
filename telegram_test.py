from news import get_news
import requests
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

message = get_news()

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "bot_token": BOT_TOKEN,
        "text": message
    }
)

print("STATUS:", r.status_code)
print("RESPONSE:", r.text)
