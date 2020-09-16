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
      json = response.json()

      for value in json['items']:
          snippet.append(value['snippet']['topLevelComment']['snippet'])
      
      nextToken = json['nextPageToken'] if 'nextPageToken' in json.keys() and (len(json['items']) > 0) else None

      if not nextToken:
          break

  ## List of comment parents in a Data frame
  df = pd.DataFrame(snippet)
  df = dropColumns(df)
  return df

def repliesDataFrame(key, videoId):
  print('Downloading replies comments...')
  nextToken = None
  replies = []
  while True:
      response = callAPI(key, videoId, 'replies', nextToken)
      json = response.json()

      for value in json['items']:
          if 'replies' in value.keys():
              for comment in value['replies']['comments']:
                  replies.append(comment['snippet'])
      
      nextToken = json['nextPageToken'] if 'nextPageToken' in json.keys() else None

      if not nextToken:
          break

  ## List of comment replies in a Data frame
  df = pd.DataFrame(replies)
  df = dropColumns(df)
  return df

def dropColumns(df):
    dropCol = ['authorProfileImageUrl', 'authorChannelUrl', 'authorChannelId', 'canRate', 'viewerRating']
    
    for col in dropCol:
        df = df.drop(col, 1)
    return df


def dataFrameToCSV(df, isParent):
  if isParent is True:
    df.to_csv(r'./data/comments_parent.csv', encoding='utf-8-sig')
    print('The table "comments_parents.csv" is saved.')
  else:
    df.to_csv(r'./data/comments_replies.csv', encoding='utf-8-sig')
    print('The table "comments_replies.csv" is saved.')