import telebot
import google.generativeai as genai

# Вставляем ключи напрямую в код
TOKEN = "8237351969:AAF3z8ZnKHHCcd2HGOI5uctyzVRR4Fv8v0k"
GEMINI_KEY = "AIzaSyAXGCO7B5EsrGxP0Xra-O_zjijLQfHMxV4"

# Настройка Gemini
genai.configure(api_key=GEMINI_KEY)
bot = telebot.TeleBot(TOKEN)
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Отправляем запрос в ИИ
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.reply_to(message, "Произошла ошибка при обращении к ИИ.")

# Запуск бота
if name == "main":
    print("Бот запущен...")
    bot.infinity_polling()
