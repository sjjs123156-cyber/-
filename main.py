import os
import telebot
from openai import OpenAI

# Вставляем твои ключи
TG_TOKEN = "8237351969:AAF3z8ZnKHHCcd2HGOI5uctyzVRR4Fv8v0k"
DEEPSEEK_KEY = "sk-e0db26397a65468b9169b70e12657024"

# Настройка клиента DeepSeek
client = OpenAI(api_key=DEEPSEEK_KEY, base_url="https://api.deepseek.com")
bot = telebot.TeleBot(TG_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Запрос к DeepSeek
        response = client.chat.completions.create(
            model="deepseek-chat", # Или deepseek-reasoner для сложных задач
            messages=[
                {"role": "system", "content": "Ты полезный ассистент."},
                {"role": "user", "content": message.text},
            ],
            stream=False
        )
        bot.reply_to(message, response.choices[0].message.content)
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.reply_to(message, "DeepSeek временно недоступен.")

if name == "main":
    print("Бот на базе DeepSeek запущен...")
    bot.infinity_polling()
