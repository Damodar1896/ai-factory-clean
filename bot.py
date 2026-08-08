import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Load environment variables from .env file
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Fetch tokens and links from .env (Damodar Tech bot)
TOKEN = os.getenv("DAMODAR_TECH_BOT_TOKEN")
BONUS_LINK = os.getenv("BONUS_LINK")
TOOL_LINK = os.getenv("TOOL_LINK")

# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_message = (
        f"नमस्कार {user_name} भाई! Damodar Tech Bot में आपका स्वागत है। 🚀\n\n"
        f"यहाँ आपको मिलेंगे बेहतरीन AI टूल्स, ऑटोमेशन और बिजनेस रिसोर्स।\n\n"
        f"📌 **नीचे दिए गए कमांड्स का उपयोग करें:**\n"
        f"👉 /bonus - अपना फ्री VIP बोनस पाने के लिए\n"
        f"👉 /pay - पेमेंट मेथड्स और QR कोड देखने के लिए\n"
        f"👉 /tools - हमारे रिकमेंडेड टूल्स देखने के लिए"
    )
    await update.message.reply_text(welcome_message, parse_mode="Markdown")

# Bonus Command
async def bonus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bonus_text = (
        f"🎁 **आपका VIP AI मास्टरगाइड बोनस तैयार है!**\n\n"
        f"नीचे दिए गए लिंक से आप इसे डाउनलोड कर सकते हैं:\n"
        f"{BONUS_LINK}"
    )
    await update.message.reply_text(bonus_text, parse_mode="Markdown")

# Tools Command
async def tools(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tools_text = (
        f"🛠️ **Recommended Business Tools:**\n\n"
        f"हमारा बेस्ट होस्टिंग और टूल प्लेटफॉर्म देखने के लिए यहाँ क्लिक करें:\n"
        f"{TOOL_LINK}"
    )
    await update.message.reply_text(tools_text, parse_mode="Markdown")

# Pay Command (Sends Payment Options & QR Codes)
async def pay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    
    info_text = (
        "💳 **Payment Methods & QR Codes:**\n\n"
        "आप नीचे दिए गए किसी भी माध्यम से पेमेंट कर सकते हैं। पेमेंट करने के बाद स्क्रीनशॉट एडमिन को भेजें।"
    )
    await context.bot.send_message(chat_id=chat_id, text=info_text, parse_mode="Markdown")

    # Send Canara Bank QR & Details
    try:
        canara_caption = f"🏦 **Canara Bank UPI**\nUPI ID: `{os.getenv('CANARA_UPI_ID')}`\nName: {os.getenv('CANARA_PAYEE_NAME')}"
        with open(os.getenv('CANARA_QR_IMAGE'), 'rb') as photo:
            await context.bot.send_photo(chat_id=chat_id, photo=photo, caption=canara_caption, parse_mode="Markdown")
    except Exception as e:
        print(f"Canara QR error: {e}")

    # Send Google Pay QR & Details
    try:
        gpay_caption = f"📱 **Google Pay (Axis Bank)**\nUPI ID: `{os.getenv('GPAY_UPI_ID')}`\nName: {os.getenv('GPAY_PAYEE_NAME')}"
        with open(os.getenv('GPAY_QR_IMAGE'), 'rb') as photo:
            await context.bot.send_photo(chat_id=chat_id, photo=photo, caption=gpay_caption, parse_mode="Markdown")
    except Exception as e:
        print(f"GPay QR error: {e}")

    # Send PhonePe QR
    try:
        phonepe_caption = f"📲 **PhonePe Business**\nName: {os.getenv('PHONEPE_PAYEE_NAME')}"
        with open(os.getenv('PHONEPE_QR_IMAGE'), 'rb') as photo:
            await context.bot.send_photo(chat_id=chat_id, photo=photo, caption=phonepe_caption, parse_mode="Markdown")
    except Exception as e:
        print(f"PhonePe QR error: {e}")

    # Send Crypto / USDT Details
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
