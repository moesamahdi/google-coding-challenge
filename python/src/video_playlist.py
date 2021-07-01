"""A video playlist class."""


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self , playlist_name: str):
        self._name = playlist_name
        self._videos = []

    @property
    def name(self) -> str:
        return self._name

    def add_video(self, video):
        self._videos.append(video)

    def get_videos(self):
        return self._videos

    def remove_video(self, video):
        self._videos.remove(video)

    def remove_all_videos(self):
        self._videos.clear()
