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

![Preview of the music recommendation system](https://user-images.githubusercontent.com/56232734/233535147-a3289944-cd47-4e5a-9c74-729d06b35dc4.jpg)

## Medium Article
You can read the steps i implemented to build this project on [Medium](https://medium.com/@ebulamicheal/how-to-build-a-music-recommendation-system-with-python-and-spotify-api-using-streamlit-5488d316aabd)

## Acknowledgements

This project was built using the [Spotipy](https://github.com/plamere/spotipy) library and the [Streamlit](https://www.streamlit.io/) framework. Special thanks to the developers of these tools for making this project possible.
