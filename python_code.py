

import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = 'INPUT YOURS'
CLIENT_SECRET = 'INPUT YOURS'
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#

def get_recommendations(track_name):
    # Get track URI
    results = sp.search(q=track_name, type='track')
    track_uri = results['tracks']['items'][0]['uri']

    # Get recommended tracks
    recommendations = sp.recommendations(seed_tracks=[track_uri])['tracks']
    return recommendations


st.title("Music Recommendation System")

# Get user input
track_name = st.text_input("Enter a song name:")

if track_name:
    # Get recommendations
    recommendations = get_recommendations(track_name)

    # Display recommended tracks with album cover
    st.write("Recommended songs:")
    for track in recommendations:
        st.write(track['name'])
        st.image(track['album']['images'][0]['url'])
