import time
import requests
from datetime import datetime

BILL_BOT_TOKEN = "8802835734:AAHIE5nYhDBHXJdX1A-ZKsoNwnMK36dTuuM"
CHAT_ID = "8482612187"

url = f"https://api.telegram.org/bot{BILL_BOT_TOKEN}/sendMessage"

days_and_bills = {
    1:"YMCA",
    10:"AES Electric",
    27:"WPCU Loan",
    23:"MEFA Loan"
}

def send_reminder(bill):
    payload = {
        "chat_id": CHAT_ID,
        "text": "Reminder: " + str(bill) + " is due today!",
        "parse_mode": "Markdown"  # Enables *bold*, `code`, etc.
    }

    response = requests.post(url, json=payload)
    print(response.json())

def main():
    day = datetime.now().day

    if day in days_and_bills:
        bill = days_and_bills[day]
        send_reminder(bill)

if __name__ == "__main__":
    main()
    
