# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:21:21 2020

@author: joamat
"""

import pandas as pd
import json
import requests


def callAPI(key, channelId, nextToken=None):
    return requests.get('https://www.googleapis.com/youtube/v3/search',
                        params={
                                'key': key,
                                'part': 'id,snippet',
                                'channelId': channelId,
                                'maxResults': 50,
                                'order': 'date',
                                'pageToken': nextToken
                                })

def dataFrameToCSV(df):
    df.to_csv(r'./data/videos_id.csv', encoding='utf-8-sig')
    print('The table "videos_id.csv" is saved.')


def videosDataFrame(key, channelId):
    print('Downloading videos Id...')
    
    nextToken = None
    snippet = []
    count=0
    while True:
        count = count + 1
        response = callAPI(key, channelId, nextToken)
        json = response.json()
        
        for value in json['items']:
            snippet.append({**value['id'], **value['snippet']})
            print(value['id'])
            
        nextToken = json['nextPageToken'] if 'nextPageToken' in json.keys() and (len(json['items']) > 0) else None

        if not nextToken:
            break
    
    print(count)

    df = pd.DataFrame(snippet)    
    return df


def dropColumns(df):
    dropCol = ['kind', 'thumbnails', 'liveBroadcastContent', 'playlistId']
    
    for col in dropCol:
        df = df.drop(col, 1)
    return df


def dropRows(df):
    df = df.dropna()
    return df


# TESTE
key = 'AIzaSyDazwNBxt816APtEYPQl5jAGg0YTRwQyPM'
channelId = 'UCUhzcbraLcYQTd3ldHBVnWA'

df = dropRows(dropColumns(videosDataFrame(key, channelId)))
print(df)
videos = dataFrameToCSV(df)