import logging
import os
import textwrap
import time

import requests
import telegram
from dotenv import load_dotenv

URl = 'https://dvmn.org/api/long_polling/'


class TelegramBotHandler(logging.Handler):

    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.tg_bot = tg_bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def check_lesson_status(timestamp, devman_token):
    headers = {'Authorization': f'Token {devman_token}'}
    payloads = {'timestamp': timestamp}
    response = requests.get(URl, headers=headers, params=payloads, timeout=120)
    response.raise_for_status()
    return response.json()


def send_message(bot, result, chat_id):
    checking_result = result['new_attempts'][0]
    title = checking_result['lesson_title']
    url = checking_result['lesson_url']

    if checking_result['is_negative']:
        text_message = f'''У вас проверили работу "{title}"
            К сожалению, в работе нашлись ошибки. ☟ 
            https://dvmn.org{url}'''
    else:
        text_message = f'''У вас проверили работу "{title}" 
            Преподавателю всё понравилось 👍, можно приступать к следующему уроку! 
            https://dvmn.org{url}'''
    bot.send_message(chat_id=chat_id, text=textwrap.dedent(text_message))


def main():
    load_dotenv()
    devman_token = os.getenv('DVMN_TOKEN')
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

    bot = telegram.Bot(token=telegram_token)

    logger = logging.getLogger('BotLogger')
    logger.setLevel(logging.INFO)
    handler = TelegramBotHandler(bot, telegram_chat_id)
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info('Бот запущен и приветствует вас!')

    timestamp = None

    while True:
        try:
            result = check_lesson_status(timestamp, devman_token)
            if result['status'] == 'timeout':
                timestamp = result['timestamp_to_request']
                continue
            timestamp = result['last_attempt_timestamp']
            send_message(bot, result, telegram_chat_id)

        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError as err:
            logger.info('Бот поймал ошибку: ')
            logger.error(err, exc_info=True)
            time.sleep(60)
            continue
        except Exception as err:
            logger.info('Бот поймал ошибку: ')
            logger.error(err, exc_info=True)


if __name__ == '__main__':
    main()
