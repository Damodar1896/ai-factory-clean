import os
import sys
import time
import telebot
from telebot import types
from dotenv import load_dotenv

# Load environment variables securely
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TOOL_LINK = os.getenv("TOOL_LINK", "https://yourdomain.com")
BONUS_LINK = os.getenv("BONUS_LINK", "https://yourdomain.com")
AFFILIATE_HUB_LINK = os.getenv("AFFILIATE_HUB_LINK", "https://yourdomain.com")
COMMUNITY_LINK = os.getenv("COMMUNITY_LINK", "https://t.me/your_channel_link")

if not TOKEN:
    print("CRITICAL ERROR: Telegram Bot Token missing!", file=sys.stderr)
    sys.exit(1)

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        markup = types.InlineKeyboardMarkup(row_width=1)
        
        # Interactive Affiliate & Resource Buttons
        btn_tools = types.InlineKeyboardButton("🎁 Free AI & Software Tools", callback_data="tools")
        btn_bonuses = types.InlineKeyboardButton("💎 VIP Exclusive Bonuses ($5k Value)", callback_data="bonuses")
        btn_affiliate = types.InlineKeyboardButton("🔥 Top Enterprise Partner Offers", callback_data="affiliate")
        btn_community = types.InlineKeyboardButton("🌐 Join Community Hub", url=COMMUNITY_LINK)
        
        markup.add(btn_tools, btn_bonuses, btn_affiliate, btn_community)
        
        welcome_text = (
            f"Welcome, {message.from_user.first_name}! 🚀\n\n"
            "You've arrived at the **Damodar Tech & AI Ecosystem Hub**.\n\n"
            "Unlock access to elite AI tools, premium software discounts, "
            "and exclusive digital resources to scale your business.\n\n"
            "Select an option below to get started:"
        )
        bot.send_message(message.chat.id, welcome_text, reply_markup=markup)
    except Exception as e:
        print(f"[Error] {e}")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == "tools":
            bot.answer_callback_query(call.id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("👉 Access Free Tools Portal", url=TOOL_LINK))
            bot.send_message(call.message.chat.id, "🎁 **Free AI & Software Resource Center**:\n\nClick below to access top-tier AI generators, scripts, and software resources:", reply_markup=markup)
            
        elif call.data == "bonuses":
            bot.answer_callback_query(call.id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("👉 Claim VIP Bonuses Now", url=BONUS_LINK))
            bot.send_message(call.message.chat.id, "💎 **Exclusive VIP Bonuses ($5,000+ Value)**:\n\nQualify for premium software templates and scaling frameworks through our partner portals:", reply_markup=markup)
            
        elif call.data == "affiliate":
            bot.answer_callback_query(call.id)
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("🚀 Browse 105+ Partner Networks", url=AFFILIATE_HUB_LINK))
            bot.send_message(call.message.chat.id, "🔥 **Top Enterprise Partner Offers (105+ Networks)**:\n\nExplore our verified high-yield partner portals (Hostinger, Binance, AI tools, etc.) to start earning instantly:", reply_markup=markup)
            
    except Exception as e:
        print(f"[Error] {e}")

if __name__ == "__main__":
    print("Damodar Tech Master Bot is running with Affiliate Engine... 24/7 Ready.")
    while True:
        try:
            bot.infinity_polling(skip_pending=True, timeout=60, long_polling_timeout=60)
        except Exception as e:
            print(f"[RECOVERY] Reconnecting in 5 seconds...")
            time.sleep(5)
