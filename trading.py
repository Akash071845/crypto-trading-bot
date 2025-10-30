from binance.client import Client
from dotenv import load_dotenv
import os
import logging



# Configure logging
logging.basicConfig(
    filename="bot_activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Load environment variables
load_dotenv()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

# Connect to Binance Futures Testnet
client = Client(api_key, api_secret, testnet=True)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'

# Test connection
try:
    server_time = client.futures_time()
    print("✅ Connected to Binance Testnet")
except Exception as e:
    print("❌ Connection failed:", e)
    exit()

# --- PLACE ORDER FUNCTION ---
def place_order(symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
        else:
            print("❌ Unsupported order type.")
            logging.warning(f"Unsupported order type: {order_type}")
            return

        print("\n✅ Order placed successfully!")
        print(order)
        logging.info(f"Order placed: {order}")

    except Exception as e:
        print("❌ Failed to place order:", e)
        logging.error(f"Order failed: {e}")

# --- USER INPUT (Command-Line Interface) ---
print("\n--- SIMPLE BINANCE TESTNET TRADING BOT ---")
symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
side = input("Buy or Sell? (BUY/SELL): ").upper()
order_type = input("Order type (MARKET/LIMIT): ").upper()
quantity = float(input("Enter quantity (e.g., 0.001): "))

price = None
if order_type == "LIMIT":
    price = float(input("Enter limit price: "))

place_order(symbol, side, order_type, quantity, price)
