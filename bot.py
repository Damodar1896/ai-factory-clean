import os
import sys
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("8658962388:AAHFohEKyLvbwQG_cbXnRQ2lG8gfa21x-Zw")

if not TOKEN:
    print("CRITICAL ERROR: Telegram Bot Token not found! Please check your .env file.", file=sys.stderr)
    sys.exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        markup = types.InlineKeyboardMarkup(row_width=1)
        
        btn_tools = types.InlineKeyboardButton("🎁 Free AI & Software Tools", callback_data="tools")
        btn_bonuses = types.InlineKeyboardButton("💎 VIP Exclusive Bonuses ($5k Value)", callback_data="bonuses")
        btn_affiliate = types.InlineKeyboardButton("🔥 Top Enterprise Partner Offers", callback_data="affiliate")
        
        markup.add(btn_tools, btn_bonuses, btn_affiliate)
        
        welcome_text = (
            f"Welcome, {message.from_user.first_name}! 🚀\n\n"
            "You've arrived at the **Damodar Tech & AI Ecosystem Hub**.\n\n"
            "Unlock access to elite AI tools, premium software discounts, "
            "and exclusive digital resources to scale your business.\n\n"
            "Select an option below to get started:"
        )
        
        bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)
    except Exception as e:
        print(f"Error in start handler: {e}")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        if call.data == "tools":
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, "🎁 Here are your Free AI Tools and Software Resource Links:")
        elif call.data == "bonuses":
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, "💎 Here are the details to claim your Exclusive VIP Bonuses ($5,000+ Value):")
        elif call.data == "affiliate":
            bot.answer_callback_query(call.id)
            bot.send_message(call.message.chat.id, "🔥 Explore our 105+ Verified Partner Networks and High-Yield Offers:")
    except Exception as e:
        print(f"Error in callback query handler: {e}")

if __name__ == "__main__":
    print("Damodar Tech Master Bot is running live and secure... 24/7 Mode Ready.")
    try:
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print(f"Bot polling crashed: {e}")
