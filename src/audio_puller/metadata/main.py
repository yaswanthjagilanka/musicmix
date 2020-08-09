"""

Script where the metadata gets finalised:


"""
from .gaana import searchSong as gaana_meta

SONG = []
options = ["gaana"] #saavn WIP

class MetaData:

    def __init__(self, SONG,title):
        """SONG is supposed to be a dict."""
        self.track_name = title
        if SONG == "nodata":
            self.track_name = SONG.track_name
            self.release_date = SONG.release_date
            self.artist_name = SONG.artist_name
            self.provider = "gaana"
            self.collection_name = SONG.collection_name
            self.primary_genre_name = SONG.primary_genre_name
            self.track_number = '1'
            self.artwork_url_100 = SONG.artwork_url_100
            self.track_time = SONG.track_time


def update_metadata(info_dict):
        gaana_meta_data = gaana_meta(info_dict['title'])
        print ("gaana meta data",gaana_meta_data)
        song_meta = MetaData(gaana_meta_data,info_dict['title'])
        song_meta.yt_tb_url = info_dict['thumbnails'][3]['url']
        print ("song_meta",song_meta.artwork_url_100 )
        return song_meta
