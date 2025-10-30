# 🚀 Simplified Binance Trading Bot (Testnet)

This project is a Python-based trading bot built for the **Binance Futures Testnet**.  
It allows users to safely place **Market** and **Limit** buy/sell orders using demo funds, showcasing API integration, error handling, and logging.

---

## ⚙️ Features
- 🔐 Connects securely to Binance Futures Testnet (USDT-M)
- 💱 Supports **Market** and **Limit** order types
- 🧠 Simple **command-line interface (CLI)** for user input
- 🧾 Structured **logging** of all trading activity and errors
- 🧰 Built with reusable, clean, and modular code

---

## 🧠 Tech Stack
- **Python 3.x**
- `python-binance`
- `dotenv`
- `logging`

---

## 🚀 How to Run
1. Clone the repository  
   ```bash
   git clone git@github.com:Akash071845/crypto-trading-bot.git
   cd crypto-trading-bot

2. Install dependencies
   ```bash
   pip install -r requirements.txt


3. Add your Binance API keys to a .env file
   ```bash
   BINANCE_API_KEY=your_api_key_here
   BINANCE_API_SECRET=your_secret_key_here


4. Run the bot
   ```bash
   python trading_bot.py
   




📊 Example Output
--- SIMPLE BINANCE TESTNET TRADING BOT ---
Enter trading pair (e.g., BTCUSDT): BTCUSDT
Buy or Sell? (BUY/SELL): BUY
Order type (MARKET/LIMIT): MARKET
Enter quantity (e.g., 0.001): 0.001

✅ Order placed successfully!
{'symbol': 'BTCUSDT', 'orderId': 10293847, 'status': 'FILLED', ...}






🧾 Logging

All API actions and errors are recorded in:

bot_activity.log




📂 Project Structure
crypto-trading-bot/
├── trading_bot.py          # Main bot logic
├── requirements.txt        # Dependencies
├── .gitignore              # Files ignored by Git
├── README.md               # Project documentation
└── bot_activity.log        # Auto-generated log file
