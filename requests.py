"""
TgBlogLeaks - Testing Bot.

Update config.py file with correct values to test it.
If you want to run a test-mode working bot, you can add "/test" after your BOT_TOKEN value in config.py.
"""

import httpx
from config import BOT_TOKEN

def compose_api_url(method) -> str:
  '''
    Returns the complete bot-api url.

    Parameters:
      method (string): bot-api method name

    Returns:
      url (string): complete bot-api url.
  '''
  return f"https://api.telegram.org/beta/{BOT_TOKEN}/{method}"

def get_updates(offset: int, limit: int) -> dict:
  '''
    Executes a getUpdates request.

    Parameters:
      offset (int): identifier of the first update to be returned
      limit (int): limits the number of updates to be retrieved

    Returns:
      result (dict): the bot-api response
  '''
  return httpx.post(
    compose_api_url("getUpdates"),
    data={
      "offset": offset,
      "limit": limit,
    }
  ).json()

def send_message(business_connection_id: str, chat_id: int, text: str) -> dict:
  '''
    Executes a sendMessage request.

    Parameters:
      business_connection_id (str): unique identifier of the business connection on behalf of which the message will be sent
      chat_id (int): unique identifier for the target chat or username of the target channel
      text (int): text of the message to be sent, 1-4096 characters after entities parsing

    Returns:
      result (dict): the bot-api response
  '''
  return httpx.post(
    compose_api_url("sendMessage"),
    data={
      "business_connection_id": business_connection_id,
      "chat_id": chat_id,
      "text": text,
      "parse_mode": "HTML"
    }
  ).json()

def send_sticker(business_connection_id: str, chat_id: int, sticker: str) -> dict:
  '''
    Executes a sendSticker request.

    Parameters:
      business_connection_id (str): unique identifier of the business connection on behalf of which the message will be sent
      chat_id (int): unique identifier for the target chat or username of the target channel
      sticker (str): sticker to send

    Returns:
      result (dict): the bot-api response
  '''
  return httpx.post(
    compose_api_url("sendSticker"),
    data={
      "business_connection_id": business_connection_id,
      "chat_id": chat_id,
      "sticker": sticker,
    }
  ).json()

def send_photo(business_connection_id: str, chat_id: int, photo: str) -> dict:
  '''
    Executes a sendPhoto request.

    Parameters:
      business_connection_id (str): unique identifier of the business connection on behalf of which the message will be sent
      chat_id (int): unique identifier for the target chat or username of the target channel
      photo (str): photo to send

    Returns:
      result (dict): the bot-api response
  '''
  return httpx.post(
    compose_api_url("sendPhoto"),
    data={
      "business_connection_id": business_connection_id,
      "chat_id": chat_id,
      "photo": photo,
    }
  ).json()

def send_document(business_connection_id: str, chat_id: int, document: str) -> dict:
  '''
    Executes a sendDocument request.

    Parameters:
      business_connection_id (str): unique identifier of the business connection on behalf of which the message will be sent
      chat_id (int): unique identifier for the target chat or username of the target channel
      document (str): document to send

    Returns:
      result (dict): the bot-api response
  '''
  return httpx.post(
    compose_api_url("sendDocument"),
    data={
      "business_connection_id": business_connection_id,
      "chat_id": chat_id,
      "document": document,
    }
  ).json()

def send_voice(business_connection_id: str, chat_id: int, voice: str) -> dict:
  '''
    Executes a sendVoice request.

    Parameters:
      business_connection_id (str): unique identifier of the business connection on behalf of which the message will be sent
      chat_id (int): unique identifier for the target chat or username of the target channel
      voice (str): voice to send

    Returns:
      result (dict): the bot-api response
  '''
  return httpx.post(
    compose_api_url("sendVoice"),
    data={
      "business_connection_id": business_connection_id,
      "chat_id": chat_id,
      "voice": voice,
    }
  ).json()

def send_video(business_connection_id: str, chat_id: int, video: str) -> dict:
  '''
    Executes a sendVideo request.

    Parameters:
      business_connection_id (str): unique identifier of the business connection on behalf of which the message will be sent
      chat_id (int): unique identifier for the target chat or username of the target channel
      video (str): video to send

    Returns:
      result (dict): the bot-api response
  '''
  return httpx.post(
    compose_api_url("sendVideo"),
    data={
      "business_connection_id": business_connection_id,
      "chat_id": chat_id,
      "video": video,
    }
  ).json()
