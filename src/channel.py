import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


"""YT_API_KEY из гугла и он вставлен в переменные окружения"""
load_dotenv()

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    """Cпециальный объект для работы с API"""
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_info = Channel.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = self.channel_info['items'][0]['snippet']['thumbnails']['default']['url']
        self.subscriberCount = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.viewCount = self.channel_info['items'][0]['statistics']['viewCount']


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        print(json.dumps(self.channel_info, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        """возвращает объект для работы с YouTube API"""
        return cls.youtube


    def to_json(self, falename):
        """сохраняющий в файл значения атрибутов экземпляра `Channel`"""

        with open(falename, "a+") as fp:
            dict_={
                'title': self.title,
                'description': self.description,
                'url': self.url,
                'subscriberCount': self.subscriberCount,
                'video_count': self.video_count,
                'viewCount': self.viewCount,
                }
            json.dump(dict_, fp, ensure_ascii=False)