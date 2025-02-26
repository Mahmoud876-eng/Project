import requests
import asyncio
from telegram import Bot

# Replace with your bot's token and chat ID
TOKEN = "7574204510:AAHDO7BlbgTVLJGNSyoBIxXQoGfqSWwd4yg"
CHAT_ID = "5944518463"

# Website URL to monitor
WEBSITE_URL = "https://example.com"

async def send_telegram_message(message):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

def check_website():
    try:
        response = requests.get(WEBSITE_URL, timeout=10)
        if response.status_code == 200:
            print("✅ Website is up")
            asyncio.run(send_telegram_message("the web site is up and running"))
        else:
            print(f"⚠️ Website error: {response.status_code}")
            asyncio.run(send_telegram_message(f"🚨 Website down! Status: {response.status_code}"))
    except requests.exceptions.RequestException:
        print("❌ Website is down!")
        asyncio.run(send_telegram_message("🚨 ALERT: The website is down!"))

if __name__ == "__main__":
    check_website()
