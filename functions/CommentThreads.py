import requests

def callAPI(key, videoId, mode, nextToken=None):
  return requests.get('https://www.googleapis.com/youtube/v3/commentThreads',
              params={
                  'key': key,
                  'part': mode,
                  'videoId': videoId,
                  'maxResults': 100,
                  'order': 'time',
                  'pageToken': nextToken
              })