import json
import requests
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Load tokens to track
def load_tokens():
    with open('tokens.json', 'r') as f:
        return json.load(f)

# Send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

# Check prices and alert
def check_prices():
    tokens = load_tokens()
    for token in tokens:
        symbol = token["symbol"]
        threshold = token["threshold"]
        price_url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"

        try:
            response = requests.get(price_url).json()
            current_price = response[symbol]["usd"]
            if current_price >= threshold:
                send_telegram_message(f"📈 {symbol.capitalize()} price is ${current_price} (≥ ${threshold})")
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")

# Scheduler to run every 5 minutes
scheduler = BlockingScheduler()
scheduler.add_job(check_prices, 'interval', minutes=5)

print("⏳ Token Price Alert Bot started...")
check_prices()  # initial run
scheduler.start()
