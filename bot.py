import os
import re
import requests
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

# Set up DeepSeek API
def generate_ai_response(user_input):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "API-KEY",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "deepseek/deepseek-r1-zero:free",
                "messages": [{"role": "user", "content": user_input}]
            })
        )
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "⚠️ Couldn't generate response. Try again.")
    except Exception as e:
        return f"⚠️ Error generating response: {e}"

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Generate Code", callback_data='generate_code')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("\U0001F916 Welcome to AI Learning Companion! Choose an option:", reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == "generate_code":
        query.message.reply_text("💻 Send me a prompt (e.g., 'Python code for prime numbers')")

def escape_markdown_v2(text):
    escape_chars = r'\_*[]()~`>#+-=|{}.!'
    return re.sub(f"([{re.escape(escape_chars)}])", r'\\\1', text)

def generate_code(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    code_output = generate_ai_response(user_input)
    safe_code_output = escape_markdown_v2(code_output)  # Escape special characters
    update.message.reply_text(f"```\n{safe_code_output}\n```", parse_mode="MarkdownV2")

def main():
    updater = Updater("TELEGRAM_BOT_API", use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, generate_code))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
