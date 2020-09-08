import requests
import pandas as pd

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

def parentsDataFrame(key, videoId):
  print('Downloading parents comments...')

  # COMMENTS
  ## Comment parents in a list
  nextToken = None
  snippet = []
  while True:
      response = callAPI(key, videoId, 'snippet', nextToken)
      
      for value in response.json()['items']:
          snippet.append(value['snippet']['topLevelComment']['snippet'])
      
      nextToken = response.json()['nextPageToken'] if 'nextPageToken' in response.json().keys() else None

      if not nextToken:
          break

  ## List of comment parents in a Data frame
  df = pd.DataFrame(snippet)
  return df

def repliesDataFrame(key, videoId):
  print('Downloading replies comments...')
  nextToken = None
  replies = []
  while True:
      response = callAPI(key, videoId, 'replies', nextToken)
      for value in response.json()['items']:
          if 'replies' in value.keys():
              for comment in value['replies']['comments']:
                  replies.append(comment['snippet'])
      
      nextToken = response.json()['nextPageToken'] if 'nextPageToken' in response.json().keys() else None

      if not nextToken:
          break

  ## List of comment replies in a Data frame
  df = pd.DataFrame(replies)
  return df

def dataFrameToCSV(df, isParent):
  if isParent is True:
    df.to_csv(r'./data/comments_parent.csv', encoding='utf-8-sig')
    print('The table "comments_parents.csv" is saved.')
  else:
    df.to_csv(r'./data/comments_replies.csv', encoding='utf-8-sig')
    print('The table "comments_replies.csv" is saved.')