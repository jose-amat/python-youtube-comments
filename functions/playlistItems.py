import requests
import pandas as pd
import json
import functions.videos as videos

def callAPI(key, playlist):
  return requests.get('https://www.googleapis.com/youtube/v3/playlistItems',
              params={
                  'key': key,
                  'part': 'snippet,contentDetails',
                  'playlistId': playlist,
                  'maxResults': 20
              })

def videosDataFrame(key, playlist):
  print('Downloading videos Id...')
  response = callAPI(key, playlist).json()['items']

  videolist = []
  for video in response:
    statistics = videos.statistics(key, video['contentDetails']['videoId'])
    videolist.append({**video['snippet']['resourceId'], **video['snippet'], **statistics})  
  return pd.DataFrame(videolist)

def dataFrameToCSV(df):
    df.to_csv(r'./data/videos_id.csv', encoding='utf-8-sig')
    print('The table "videos_id.csv" is saved.')
