# pip install python-telegram-bot requests

# https://api.football-data.org/v4/matches
import requests

def get_match_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def process_match_data(match_data):
    goals = {}
    for match in match_data['matches']:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        score = match['score']['fullTime']
        goals[(home_team, away_team)] = score
    return goals

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Функция для отправки уведомлений
def send_notification(context: CallbackContext, chat_id, message):
    context.bot.send_message(chat_id=chat_id, text=message)

# Функция для старта бота
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я буду уведомлять тебя о количестве забитых голов в футбольных матчах.')

# Функция для мониторинга матчей
def monitor_matches(context: CallbackContext):
    api_url = 'https://api.football-data.org/v2/matches'  # Пример URL
    match_data = get_match_data(api_url)
    if match_data:
        goals = process_match_data(match_data)
        for (home_team, away_team), score in goals.items():
            message = f'Матч: {home_team} vs {away_team}\nСчет: {score["homeTeam"]} - {score["awayTeam"]}'
            send_notification(context, context.job.context, message)

def main():
    # Токен вашего Telegram бота
    updater = Updater('7757426223:AAGSRzxVPMzklzy5ZgRJRC8o6KXvB5Q2YNE', 100)

    dp = updater.dispatcher

    # Обработчик команды /start
    dp.add_handler(CommandHandler("start", ))

    # Запуск мониторинга матчей каждые 5 минут
    job_queue = updater.job_queue
    job_queue.run_repeating(monitor_matches, interval=300, first=0, context=YOUR_CHAT_ID)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
