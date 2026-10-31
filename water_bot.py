# Water Bot Reminder
import time
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

WATER_BOT_TOKEN = "9120042771:AAHgxAG7YWNpg5Uz__Va1gC7MScLR32qdI0"
TYLERS_CHAT_ID = "8482612187"
TORIS_CHAT_ID = "9017353348"

tyler_checkpoints = {
    "7:00":"⌚**It's 7:00!**\n☀️ **Morning Wake-Up Checkpoint**\n🎯 **Current Target:** 24 oz (1 Stanley) by 11:00\n\n*Drink a full glass before coffee or breakfast!*\n\n📊 **Day Total:** 24 / 96 oz (1 / 4 Stanley)",
    "11:00":"⌚**It's 11:00!**\n⏰ **Late Morning Checkpoint**\n🎯 **Current Target:** 12 oz (0.5 Stanley) by 15:00\n\n*Halfway to your afternoon block! Keep steady.*\n\n📊 **Day Total:** 36 / 96 oz (1.5 / 4 Stanley)",
    "15:00":"⌚**It's 15:00!**\n⚡ **Mid-Afternoon Checkpoint**\n🎯 **Current Target:** 24 oz (1 Stanley) by 19:00\n\n*Finish a full 40 oz tumbler to beat the 3 PM fatigue.*\n\n📊 **Day Total:** 60 / 96 oz (2.5 / 4 Stanley)",
    "19:00":"⌚**It's 19:00!**\n🍽️ **Dinner Time Checkpoint**\n🎯 **Current Target:** 24 oz (1 Stanley) by 21:00\n\n*Almost done for the day! Wrap up heavy fluid intake.*\n\n📊 **Day Total:** 84 / 96 oz (3.5 / 4 Stanley)",
    "21:00":"⌚**It's 21:00!**\n🌙 **Bedtime Final Checkpoint**\n🎯 **Current Target:** 12 oz (0.5 Stanley) by 24:00\n\n*Just small sips if needed before sleep.*\n\n📊 **Day Total:** 96 / 96 oz (4 / 4 Stanley)🎉",
}

tori_checkpoints = {
    "7:00":"⌚**It's 7:00!**\n☀️ **Morning Wake-Up Checkpoint**\n🎯 **Current Target:** 16 oz (0.5 Stanley) by 11:00\n\n*Drink a full glass before coffee or breakfast!*\n\n📊 **Day Total:** 16 / 64 oz (0.5 / 2 Stanley)",
    "11:00":"⌚**It's 11:00!**\n⏰ **Late Morning Checkpoint**\n🎯 **Current Target:** 8 oz (0.25 Stanley) by 15:00\n\n*Halfway to your afternoon block! Keep steady.*\n\n📊 **Day Total:** 24 / 64 oz (0.75 / 2 Stanley)",
    "15:00":"⌚**It's 15:00!**\n⚡ **Mid-Afternoon Checkpoint**\n🎯 **Current Target:** 16 oz (0.5 Stanley) by 19:00\n\n*Finish a full 24 oz tumbler to beat the 3 PM fatigue.*\n\n📊 **Day Total:** 40 / 64 oz (1.25 / 2 Stanley)",
    "19:00":"⌚**It's 19:00!**\n🍽️ **Dinner Time Checkpoint**\n🎯 **Current Target:** 16 oz (0.5 Stanley) by 21:00\n\n*Almost done for the day! Wrap up heavy fluid intake.*\n\n📊 **Day Total:** 56 / 64 oz (1.75 / 2 Stanley)",
    "21:00":"⌚**It's 21:00!**\n🌙 **Bedtime Final Checkpoint**\n🎯 **Current Target:** 8 oz(0.25 Stanley) by 24:00\n\n*Just small sips if needed before sleep.\n\n📊 **Day Total:** 64 / 64 oz (2 / 2 Stanley)🎉"
}

url = f"https://api.telegram.org/bot{WATER_BOT_TOKEN}/sendMessage"

def send_reminders(hour):
    tylers_payload = {
        "chat_id": TYLERS_CHAT_ID,
        "text": tyler_checkpoints[hour],
        "parse_mode": "Markdown"  # Enables *bold*, `code`, etc.
    }
    response = requests.post(url, json=tylers_payload)

    toris_payload = {
        "chat_id": TORIS_CHAT_ID,
        "text": tori_checkpoints[hour],
        "parse_mode": "Markdown"  # Enables *bold*, `code`, etc.
    }
    response = requests.post(url, json=toris_payload)

def main():
    while True:     
        current_time = datetime.now(ZoneInfo("America/New_York")).strftime("%H:%M")
        
        if current_time in tyler_checkpoints:
            send_reminders(current_time)

        time.sleep(60)

if __name__ == "__main__":
    main()
