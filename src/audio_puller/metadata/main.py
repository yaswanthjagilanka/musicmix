"""

Script where the metadata gets finalised:


"""
from gaana import searchSong as gaana_meta

SONG = []
options = ["gaana"] #saavn WIP

class MetaData:

    def __init__(self, SONG):
        """SONG is supposed to be a dict."""
        self.track_name = SONG['track_title']
        self.release_date = SONG['release_date']
        self.artist_name = SONG['artist'][0]['name']
        self.provider = "gaana"
        self.collection_name = SONG['album_title']
        self.primary_genre_name = SONG['gener'][0]['name']
        self.track_number = '1'
        self.artwork_url_100 = SONG['artwork_large']
        self.track_time = self._convert_time(SONG['duration'])


    def update_metadata(self, title):
        self.gaana_data = gaana_meta(title)
        pass