import telebot
from telebot import types
import importlib
from dotenv import load_dotenv
import os

# Загрузить переменные окружения из файла .env
load_dotenv()

# Получить токен из переменной окружения
API_KEY = os.getenv('TELEGRAM_API_KEY')
bot = telebot.TeleBot(API_KEY)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item1 = types.KeyboardButton("Садовая 8, п. 1")
    markup.add(item1)
    
    bot.send_message(
        message.chat.id,
        "Какую дверь открыть?",
        reply_markup=markup
    )

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Садовая 8, п. 1":
        openDoor('sadovaya8_1')
        bot.reply_to(message, f"Вы открыли дверь {message.text}")
    else:
        bot.reply_to(message, "Пожалуйста, выберите одну из доступных дверей.")

def openDoor(door):
    module_name = f"doors.{door}"
    module = importlib.import_module(module_name)
    if hasattr(module, 'open'):
        module.open()
    else:
        print(f"Модуль {module_name} не имеет функции open()")

# Запуск бота
bot.polling()