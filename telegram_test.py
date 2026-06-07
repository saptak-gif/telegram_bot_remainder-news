import requests

BOT_TOKEN = "8565676723:AAEKEI3w9oakwnMiw6kE6U2wbWqVxHs6S5I"
CHAT_ID = "7105064562"

message = """
Good morning!

• AI News
• Tech News
• Internship Updates
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": 7105064562,
        "text": message
    }
)