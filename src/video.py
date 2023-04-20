import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


"""YT_API_KEY из гугла и он вставлен в переменные окружения"""
load_dotenv()

class Video:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    """Cпециальный объект для работы с API"""
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, video_id: str) -> None:
        """Bнициализация реальных данных атрибутов экземпляра класса `Video`"""
        self.video_id = video_id
        self.video_info = Video.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                       id=video_id
                                       ).execute()
        self.video_title: str = self.video_info['items'][0]['snippet']['title']
        self.video_url = self.video_info['items'][0]['snippet']['thumbnails']['default']['url']
        self.view_count: int = self.video_info['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_info['items'][0]['statistics']['likeCount']
        self.comment_count: int = self.video_info['items'][0]['statistics']['commentCount']

    def __str__(self):
        return f'"{self.video_title}"'

class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id) -> None:
        super().__init__(video_id)
        """Инициализация реальных данных атрибутов экземпляра класса `PLVideo`"""
        self.playlist_id = playlist_id
        self.playlist_videos = PLVideo.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]



