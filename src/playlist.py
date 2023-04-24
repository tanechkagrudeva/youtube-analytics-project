import datetime
import isodate
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

class PlayList:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    """Cпециальный объект для работы с API"""
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __init__(self, playlist_id: str) -> None:
        self.playlist_id = playlist_id

        self.playlist_info = PlayList.youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails, snippet',
                                                       maxResults=50,
                                                       ).execute()
        self.title: str = self.playlist_info['items'][0]['snippet']['title']
        self.url = "https://www.youtube.com/playlist?list=" + playlist_id
        self.video_response = PlayList.youtube.videos().list(part='contentDetails,statistics',
                                                   id=','.join(self.playlist_id)
                                                   ).execute()

    @property
    def total_duration(self):
        """возвращает объект класса `datetime.timedelta`
        с суммарной длительность плейлиста (обращение как к свойству, использовать `@property`"""

        total_duration = datetime.timedelta(seconds=0)

        for dis_video in self.video_response['items']:
            iso_8601_duration = dis_video['contentDetails']['duration']
            duration_video = isodate.parse_duration(iso_8601_duration)
            total_duration += duration_video

        return total_duration

    def show_best_video(self):
        """возвращает ссылку на самое популярное видео из плейлиста (по количеству лайков)"""
        popular_like = 0
        url = None
        for video in self.video_answer['items']:
            like_count: int = video['statistics']['likeCount']
            if popular_like < like_count:
                popular_like = like_count
                url = "https://youtu.be/" + video['id']
        return url
