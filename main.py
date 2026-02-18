import os
import telebot
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Инициализация
client = genai.Client(api_key=os.environ.get('GEMINI_KEY'))
bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        # Новый метод вызова в библиотеке google-genai
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=message.text
        )
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    print("Бот на обновленном Gemini запущен!")
    bot.infinity_polling()
  
