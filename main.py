import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import src.soporteClean as sc
import src.soporteImagenes as si
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

tracks = sc.importDatasets()

st.markdown(f'# Hi there')
st.image('https://64.media.tumblr.com/da7235613f6fe6292360d74d410ece3b/01bebaf99b141ae6-a4/s500x750/1070b19f89a4cc2c1b3420495fb027fcfb1acc9f.gif')
st.markdown("""
This is an investigation based on the `top 200` and `viral 50` spotify playlists on the USA region between 2017 and 2021 to see if there's a significant change on the musics upliftness.

In the old days, to consider a song `happy` the main ingredients where a fast tempo and a major key -- such was the case of some of the Beatles 70's songs.

Los resultados para she loves you de los beatles // don't stop me now de queen-- quiero hacer un chart radial desos chulos

However, as time passes, now this songs are considered cheesy and now there's a bigger mixture between tempo and keys. 

For measuring that, the psychologis Jacob Jojil created the `Feel Good Index`, 
>(Jolij's) Final equation of Feel Good Index (FGI) includes the sum of all positive references in the lyrics, the song's tempo in beats per minute and its key. The higher a song's FGI, the more feel-good it is predicted to be. Happy lyrics, a fast tempo of 150 beats per minute (the average pop song has a tempo of 116 beats per minute), and a major third musical key all help create music we perceive as brimming with positive emotion.

Is there a magic recipe to get the mood in popular music and see if there was a turning point on the Covid-19 pandemic?

This analysis will take the given variables into account: 
- `Valence` is considered as how positive the music is percieved, being 1 the most positive and 0 the most negative
- `Energy` is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
- `Danceability` describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- The `tempo` the track is. The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
- The `key` the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.  
- `Mode` indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived.
- `Lyrics` as if the song has relation to any positive/negative elements. 
""")
