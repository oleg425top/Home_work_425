from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text('Привет! Я ваш бот.')

# Функция для обработки текстовых сообщений
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Токен вашего Telegram бота
    updater = Updater('7757426223:AAGSRzxVPMzklzy5ZgRJRC8o6KXvB5Q2YNE')

    # Получение диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрация обработчика для команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрация обработчика для текстовых сообщений
    dp.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    # Запуск бота
    updater.start_polling()

    # Ожидание завершения работы бота
    updater.idle()

if __name__ == '__main__':
    main()

