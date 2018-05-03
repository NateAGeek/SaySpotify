import spotipy;
import sys;
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

def get_word(word):

    for x in range(0, 100):
        tracks = sp.search("track:" + word, limit=50, offset=x*50);
        for item in tracks['tracks']['items']:
            lowercase = item['name'].lower();
            if lowercase == word:
                return item

    return 0;


sp = spotipy.Spotify(auth='****');

sen = sys.argv[1];
sen_words = sen.split();

print("Making playlist of sentence: " + sen);
playlist = sp.user_playlist_create(122350004, sen, True);
playlist_id = playlist['id'];

tracks = []

for word in sen_words:
    spot_word = get_word(word.lower())
    if spot_word != 0:
        print("Track: " + spot_word['name'] + ", Artist: " + spot_word['artists'][0]['name']);
        tracks.append(spot_word['id'])

sp.user_playlist_add_tracks(122350004, playlist_id, tracks);
print("Done");



