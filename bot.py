import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Fetch tokens and links
TOKEN = os.getenv("DAMODAR_TECH_BOT_TOKEN")
BONUS_LINK = os.getenv("BONUS_LINK")
TOOL_LINK = os.getenv("TOOL_LINK")

# Start Command (English)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_message = (
        f"Hello {user_name} bhai! Welcome to Damodar Tech Bot. 🚀\n\n"
        f"Here you will get the best AI tools, automation, and business resources.\n\n"
        f"📌 **Use the commands below:**\n"
        f"👉 /bonus - To get your free VIP bonus\n"
        f"👉 /pay - To view payment methods & QR codes\n"
        f"👉 /tools - To check our recommended tools"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

# Bonus Command (English & Clean Link)
async def bonus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bonus_text = (
        f"🎁 **Your VIP AI Masterguide Bonus is ready!**\n\n"
        f"You can download or view it directly from the link below:\n"
        f"{BONUS_LINK}"
    )
    await update.message.reply_text(bonus_text, parse_mode="Markdown")

# Tools Command (English)
async def tools(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tools_text = (
        f"🛠️ **Recommended Business Tools:**\n\n"
        f"Click here to check out our best hosting and tool platform:\n"
        f"{TOOL_LINK}"
    )
    await update.message.reply_text(tools_text, parse_mode="Markdown")

# Pay Command (Sends ONLY 2 Options: UPI & Crypto)
async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    info_text = (
        "💳 **Payment Options:**\n\n"
        "Choose your preferred payment method below. After payment, send the screenshot to the admin."
    )
    await context.bot.send_message(chat_id=chat_id, text=info_text, parse_mode="Markdown")

    # 1. Send Google Pay / UPI QR (Only 1 clean UPI option)
    try:
        gpay_caption = f"📱 **UPI / Google Pay**\nUPI ID: `{os.getenv('GPAY_UPI_ID')}`\nName: {os.getenv('GPAY_PAYEE_NAME')}"
        with open(os.getenv('GPAY_QR_IMAGE'), 'rb') as photo:
            await context.bot.send_photo(chat_id=chat_id, photo=photo, caption=gpay_caption, parse_mode="Markdown")
    except Exception as e:
        print(f"UPI QR error: {e}")

    # 2. Send Crypto / USDT QR (Only 1 Crypto option)
    try:
        crypto_caption = (
            f"₿ **Crypto / USDT Payment**\n"
            f"Wallet Address:\n`{os.getenv('CRYPTO_BTC_WALLET')}`\n\n"
            f"{os.getenv('PAYMENT_INSTRUCTIONS')}"
        )
        with open(os.getenv('CRYPTO_QR_IMAGE'), 'rb') as photo:
            await context.bot.send_photo(chat_id=chat_id, photo=photo, caption=crypto_caption, parse_mode="Markdown")
    except Exception as e:
        print(f"Crypto QR error: {e}")

def main():
    if not TOKEN:
        print("Error: Damodar Tech Bot Token is missing in .env file!")
        return

    application = ApplicationBuilder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("bonus", bonus))
    application.add_handler(CommandHandler("tools", tools))
    application.add_handler(CommandHandler("pay", pay))

    print("🤖 Damodar Tech Bot is starting and polling for messages...")
    application.run_polling()

if __name__ == "__main__":
    main()
