"""
TgBlogLeaks - Testing Bot.

Update config.py file with correct values to test it.
If you want to run a test-mode working bot, you can add "/test" after your BOT_TOKEN value in config.py.
"""

import json
from html import escape

import sentry_sdk

from config import HANDLE_ERRORS_WITH_SENTRY, SENTRY_DSN
from requests import (
  get_updates,
  send_message,
  send_photo,
  send_sticker,
  send_video
)

def main():
  '''
    Runs the event handler.

    Parameters:
      empty

    Returns:
      empty
  '''

  offset = 0
  while True:
    try:
      updates = get_updates(
        offset=offset,
        limit=100
      )

      for update in updates['result']:
        if 'update_id' in update:
          offset = update['update_id'] + 1

        if 'business_message' in update and 'business_connection_id' in update['business_message']:
          if 'text' in update['business_message']:
            business_connection_id = update['business_message']['business_connection_id']
            chat_id = update['business_message']['chat']['id']
            message_text = update['business_message']['text']

            if message_text == '/test':
              send_message(
                business_connection_id,
                chat_id,
                "Ready! Yuppy"
              )
            elif message_text == '/update':
              send_message(
                business_connection_id,
                chat_id,
                f"<pre language=\"json\">{escape(json.dumps(update, indent=4))}</pre>",
              )
            elif message_text == '/premium':
              send_message(
                business_connection_id,
                chat_id,
                "<tg-emoji emoji-id=\"5064415372887719937\">👍</tg-emoji><tg-emoji emoji-id=\"5062209838461747201\">👍</tg-emoji><tg-emoji emoji-id=\"5062599890211700737\">👍</tg-emoji>",
              )
            elif message_text == '/photo':
              send_photo(
                business_connection_id,
                chat_id,
                "https://images.unsplash.com/photo-1554080353-a576cf803bda?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGhvdG98ZW58MHx8MHx8fDA%3D",
              )
            elif message_text == '/video':
              send_video(
                business_connection_id,
                chat_id,
                "https://file-examples.com/storage/fe17d655216606dd89d5226/2017/04/file_example_MP4_480_1_5MG.mp4",
              )
            elif message_text == '/sticker':
              send_sticker(
                business_connection_id,
                chat_id,
                "CAACAgEAAxkBAAM2ZgbSQjarj_ikHWNKc5Mju3CGJssAAgEAA-sy6EfceyHdrvmpHjQE",
              )
              send_sticker(
                business_connection_id,
                chat_id,
                "CAACAgEAAxkBAAOAZgc8kRyKWCwp-cJeUJPBPCWuC0YAAgEAA5n0-UaraZRX71LLsDQE",
              )

    except Exception as e: # pylint: disable=broad-exception-caught
      if HANDLE_ERRORS_WITH_SENTRY and SENTRY_DSN:
        sentry_sdk.capture_exception(e)


if HANDLE_ERRORS_WITH_SENTRY and SENTRY_DSN:
  sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
  )

main()
