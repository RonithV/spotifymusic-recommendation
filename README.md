# Music Recommendation System

This is a simple music recommendation system built using [Streamlit](https://www.streamlit.io/) and the [Spotify Web API](https://developer.spotify.com/documentation/web-api/).

## How it works

The user inputs a song name and the system returns a list of recommended songs based on that input. The recommended songs are displayed with their album covers.

## Setup

Before running the application, you need to set up your Spotify credentials. 

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create a new app.

2. Copy your client ID and client secret to the `client_id` and `client_secret` variables in the `app.py` file.

3. Install the necessary packages by running `pip install -r requirements.txt`.

4. Run the app using `streamlit run app.py`.

## Preview

![Preview of the music recommendation system]

## Acknowledgements

This project was built using the [Spotipy](https://github.com/plamere/spotipy) library and the [Streamlit](https://www.streamlit.io/) framework. Special thanks to the developers of these tools for making this project possible.
