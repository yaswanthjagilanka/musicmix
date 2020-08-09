"""
Python module to search gaana.com using their API.

Uses api.gaana.com to get search results.
"""

import requests

# Define the base url
base_url = "http://api.gaana.com/?type=search&subtype=search_song&key={}&token=b2e6d7fbc136547a940516e9b77e5990&format=JSON"

SONG = []


class GaanaSongs():
    """Class to store gaana song tags."""

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

    def _convert_time(self, duration):
        in_min = int(duration)
        in_time = int(in_min / 60) + (0.01 * (in_min % 60))
        return in_time


def searchSong(querry, lim=40):
    """Nanan."""
    querry = query_set(querry)
    print ("querry",querry)
    url = base_url.format(querry)
    r = requests.get(url)
    data = r.json()
    data = data['tracks']
    print (data)
    SONG_TUPLE = []

    if data:
        for i in range(0, len(data)):
            song_obj = GaanaSongs(data[i])
            SONG_TUPLE.append(song_obj)
    if not SONG_TUPLE:
        data = None
    else:
        data = SONG_TUPLE[0]
    return data

def query_set(querry):
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

# if __name__ == '__main__':
#     q = input("Enter the querry: ")
#     dat = searchSong(q)
#     print (dat)
    # for i in range(0, len(dat)):
    #     print(dat[i].collection_name)
