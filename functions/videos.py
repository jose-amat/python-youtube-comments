import requests
import pandas as pd
import json

def callAPI(key, videoId):
  return requests.get('https://www.googleapis.com/youtube/v3/videos',
              params={
                  'key': key,
                  'part': 'statistics',
                  'id': videoId
              })

def statistics(key, videoId):
    response = callAPI(key, videoId).json()
    statistics = response['items'][0]['statistics']
    return statistics

