import logging
import os
import time

import requests
import telegram
from dotenv import load_dotenv

load_dotenv()

URl = 'https://dvmn.org/api/long_polling/'
DEVMAN_TOKEN = os.getenv('DVMN_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def initialize_logger():
    logging.basicConfig(
        filename='bot.log',
        filemode='w',
        level=logging.INFO,
        format='%(filename)s - %(name)s - %(levelname)s - %(message)s')


def check_lesson_status(timestamp):
    headers = {'Authorization': f'Token {DEVMAN_TOKEN}'}
    payloads = {'timestamp': timestamp}
    response = requests.get(URl, headers=headers, params=payloads, timeout=50)
    response.raise_for_status()
    return response.json()


def send_message(bot, result):
    checking_result = result['new_attempts'][0]
    title = checking_result['lesson_title']
    url = checking_result['lesson_url']

    if checking_result['is_negative']:
        bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=f'У вас проверили работу "{title}" \n'
                 f'К сожалению, в работе нашлись ошибки. ☟\n'
                 f'https://dvmn.org{url}')
    else:
        bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=f'У вас проверили работу "{title}" \n'
                 f'Преподавателю всё понравилось 👍, можно приступать к следующему уроку! \n'
                 f'https://dvmn.org{url}')


def main():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    timestamp = None

    while True:
        try:
            result = check_lesson_status(timestamp)
            if result['status'] == 'timeout':
                timestamp = result['timestamp_to_request']
            timestamp = result['last_attempt_timestamp']
            send_message(bot, result)

        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError as err:
            logging.info(f'Ошибка подключения, нет сети {err}')
            time.sleep(60)
            continue


if __name__ == '__main__':
    initialize_logger()
    main()
