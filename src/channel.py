import json
import os

from googleapiclient.discovery import build


"""YT_API_KEY из гугла и он вставлен в переменные окружения"""

os.environ['YT_API_KEY'] = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
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

    def get_service(self):
        """возвращает объект для работы с YouTube API"""
        id_channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        title_channel = youtube.channels().list(snippet=self.channel_id, part='title').execute()
        description_channel = youtube.channels().list(snippet=self.channel_id, part='description').execute()
        url = youtube.channels().list(snippet=self.channel_id, part='thumbnails, default, url').execute()
        subscriberCount = youtube.channels().list(statistics=self.channel_id, part='subscriberCount').execute()
        video_count = youtube.channels().list(statistics=self.channel_id, part='videoCount').execute()
        viewCount = youtube.channels().list(statistics=self.channel_id, part='viewCount').execute()
        return id_channel, title_channel, description_channel, url, subscriberCount, video_count, viewCount

    def to_json(self):
        """сохраняющий в файл значения атрибутов экземпляра `Channel`"""
        with open('vdud.json', 'w') as outfile:
            json.dump(Channel.get_service(), outfile)