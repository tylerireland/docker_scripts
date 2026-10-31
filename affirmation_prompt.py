import requests
import smtplib as smtp
from email.mime.text import MIMEText
from datetime import datetime
import linecache

TOKEN = "8696119593:AAFfYX23sdIJNaZyH-Dw0Y_oHPXazDuUYX8"
CHAT_ID = "8482612187"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

day = datetime.now().timetuple().tm_yday
prompt = linecache.getline("prompts.txt", day)

payload = {
    "chat_id": CHAT_ID,
    "text": prompt,
    "parse_mode": "Markdown"  # Enables *bold*, `code`, etc.
}

response = requests.post(url, json=payload)
print(response.json())