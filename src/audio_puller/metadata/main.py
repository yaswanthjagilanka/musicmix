"""

Script where the metadata gets finalised:


"""
from .gaana import searchSong as gaana_meta
from .saavn import search_from_query as saavn_meta
from .ytmt import yt_meta

SONG = []
options = ["gaana"] #saavn WIP

class MetaData:

    def __init__(self, SONG,provider):
        """SONG is supposed to be a dict."""
        self.track_name = SONG.track_name
        self.release_date = SONG.release_date
        self.artist_name = SONG.artist_name
        self.provider = provider
        self.lanugage = SONG.language
        self.album_title = SONG.album_title
        self.lyrics_url = SONG.lyrics_url
        self.youtube_id = SONG.youtube_id
        self.collection_name = SONG.collection_name
        self.primary_genre_name = SONG.primary_genre_name
        self.artwork_url = SONG.artwork_url_100
        self.track_time = SONG.track_time


def update_metadata(info_dict):
        #title process before meta collection
        query = query_preprocess(info_dict['title'])
        print ("query is {}".format(query))
        #meta process yt
        yt_meta_data = yt_meta(info_dict)
        #meta process saavn
        # saavn_meta_data = saavn_meta(query)
        saavn_meta_data = None
        # print ("ssaavn",saavn_meta_data)
        #meta process gaana
        gaana_meta_data = gaana_meta(query)
        # print ("gaana_meta in main : {}".format(gaana_meta_data))
        #final meta collection
        final_meta = meta_final(yt_meta_data,saavn_meta_data,gaana_meta_data)
        #return song_meta
        return final_meta

def query_preprocess(querry):
    querry = querry.replace("Video ","")
    querry = querry.replace("video ","")
    querry = querry.replace("song ","")
    querry = querry.replace("Song ","")
    querry = querry.replace("Songs","")
    querry = querry.replace("Movie ","")
    querry = querry.replace(" _ ","")
    querry = querry.replace(" -","")
    querry = querry.replace("| ","")
    querry = querry.replace("  ","")
    querry = querry.replace("Full","")
    querry = querry.replace("HD ","")
    return querry[:40]

def meta_final(yt_meta_data,saavn_meta_data,gaana_meta_data):
    if gaana_meta_data:
        meta_final = MetaData(gaana_meta_data,"gaana")
    else:
        meta_final= MetaData(yt_meta_data,"yt")
    return meta_final