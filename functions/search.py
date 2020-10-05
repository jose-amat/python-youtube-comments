# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:21:21 2020

@author: joamat
"""

import pandas as pd
import json
import requests
import functions.videos as videos

def callAPI(key, channelId, order):
    return requests.get('https://www.googleapis.com/youtube/v3/search',
                        params={
                                'key': key,
                                'part': 'id,snippet',
                                'channelId': channelId,
                                'maxResults': 6,
                                'order': order
                                })

def dataFrameToCSV(df):
    df.to_csv(r'./data/videos_id.csv', encoding='utf-8-sig')
    print('The table "videos_id.csv" is saved.')


def videosDataFrame(key, channelId, order):
    print('Downloading videos Id...')
    response = callAPI(key, channelId, order)
    json = response.json()
    snippet = []    
    for value in json['items']:
        if 'videoId' in value['id'].keys():
            statistics = videos.statistics(key, value['id']['videoId'])
            snippet.append({**value['id'], **value['snippet'], **statistics})
            print(value['id'])

    df = pd.DataFrame(snippet)    
    return df


def dropColumns(df):
    dropCol = ['kind', 'thumbnails', 'liveBroadcastContent', 'channelTitle']
    
    for col in dropCol:
        df = df.drop(col, 1)
    return df


def dropRows(df):
    df = df.dropna(subset=['videoId'])
    return df
