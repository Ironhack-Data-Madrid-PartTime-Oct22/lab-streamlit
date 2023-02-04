import pickle
import pandas as pd
import src.biblioteca as bb 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import scipy

def sentiment(lyrics):
    if type(lyrics) == 'float':
        return '', np.nan
    else:
        analyser = SentimentIntensityAnalyzer()
        sentiment_score = analyser.polarity_scores(lyrics)
        if sentiment_score['compound'] >= 0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Positive'
            return sentiment, sentiment_percentage
        elif sentiment_score['compound'] > -0.05 and sentiment_score['compound'] < 0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Neutral'
            return sentiment, sentiment_percentage
        elif sentiment_score['compound'] <= -0.05:
            sentiment_percentage = sentiment_score['compound']
            sentiment = 'Negative'
            return sentiment, sentiment_percentage

def importDatasets():
    with open('data/playlist.pickle', 'rb') as base_data:
        base_data = pickle.load(base_data)
    with open('data/spotify.pickle', 'rb') as data_spotify:
        data_spotify = pickle.load(data_spotify)
    data_spotify.drop_duplicates(inplace=True)
    with open('data/lastfm.pickle', 'rb') as data_lastfm:
        data_lastfm = pickle.load(data_lastfm)
    data_lastfm.drop_duplicates(inplace=True)
    with open('data/genius.pickle', 'rb') as data_genius:
        data_genius = pickle.load(data_genius)
    df = base_data.merge(data_lastfm, on = 'url', indicator = True, how = 'left')
    df.drop(['_merge'], axis = 1, inplace = True)
    df = df.merge(data_spotify, on = 'url', indicator = True, how = 'left')
    df.drop(['artist_y', 'track_x', 'artist', 'track_y', '_merge'], axis = 1, inplace= True)
    df.rename({'artist_x':'artist', 'date_x':'playlist_date', 'date_y':'release_date'}, inplace=True, axis=1)
    df = df.merge(data_genius, on = 'url', indicator = True, how = 'left')
    df.drop(['_merge'], axis = 1, inplace= True)
    df['playlist_date'] = pd.to_datetime(df['playlist_date'])
    df['month'] = df['playlist_date'].dt.month
    df['year'] = df['playlist_date'].dt.year
    df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str)
    df['key_mapped'] = df['key'].replace(bb.dict_keys)
    df['mode_mapped'] = df['mode'].replace(bb.dict_scale)
    df['scale'] = df['key_mapped'] + ' ' + df['mode_mapped']
    keys_scale = bb.dict_keys_scale
    dict_keys_scale = {
        'scale':list(keys_scale.keys()),
        'mapping':list(keys_scale.values())
    }
    df_keys_scale = pd.DataFrame(dict_keys_scale)
    df_keys_scale[['sentiment_key', 'sentiment_ratio_key']] = df_keys_scale.apply(lambda x: sentiment(x.mapping), axis=1, result_type='expand')
    df = df.merge(df_keys_scale[['scale', 'sentiment_ratio_key']], on = 'scale')
    return df

def columnasHomogeneas(df):
    num = df.select_dtypes(exclude='object', include='float').apply(scipy.stats.zscore).abs()
    text = df.select_dtypes(include='object')
    return pd.concat([text, num], axis=1)


def info_artists(df):
    top10_artists = df.groupby(['artist'])['streams'].sum().reset_index().sort_values(by = 'streams', ascending = False).head(5)
    top10_artists['ratio'] = top10_artists['streams'] * 100 / (df[~df['streams'].isnull()]['streams'].sum())
    return top10_artists

def info_genre(df):
    top10_musicgenre = df.groupby(['music_genre'])['streams'].sum().reset_index().sort_values(by = 'streams', ascending = False).head(5)
    top10_musicgenre['ratio'] = top10_musicgenre['streams'] * 100 / (df[~df['streams'].isnull()]['streams'].sum())
    return top10_musicgenre