import json
import os

from googleapiclient.discovery import build


"""YT_API_KEY из гугла и он вставлен в переменные окружения"""

os.environ['YT_API_KEY'] = 'AIzaSyA-sSEqG6U99YLuZn_X3bZ3mA830RlHBGA'
api_key: str = os.getenv('YT_API_KEY')

"""Cпециальный объект для работы с API"""
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
