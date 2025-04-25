# 🪙 Token Price Alert Bot (Python)

This bot monitors the prices of selected tokens and sends Telegram alerts when the price crosses a specified threshold.

---

## 🚀 Features
- Supports multiple tokens
- Uses CoinGecko API (no API key required)
- Sends alerts via Telegram bot
- Easy to configure via `tokens.json`
- Scheduled checks using APScheduler

---

## 📦 Requirements

- Python 3.7+
- Telegram bot token and chat ID

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 📦 Setup Instructions
1. Clone or download the bot files
```bash
git clone https://github.com/your-repo/token-alert-bot.git
cd token-alert-bot

```

2. Create a Telegram Bot
Message @BotFather on Telegram

Use /newbot to create a bot and get the Bot Token

3. Get your Chat ID
Message your bot once

Open: https://api.telegram.org/bot<YourBotToken>/getUpdates

Copy the chat.id from the response

4. Configure your tokens and thresholds
Edit tokens.json

5. Add your secrets in .env

## ▶️ Run the Bot
```bash
python bot.py

```
