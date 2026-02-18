import os
import telebot
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Ключи будем брать из настроек Render (это безопасно)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
GEMINI_KEY = os.environ.get('GEMINI_KEY')

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    bot.infinity_polling()
