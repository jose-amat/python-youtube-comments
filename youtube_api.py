# Importing packages
import functions.CommentThreads as ct
import csv
import pandas as pd

# videoId = '85YoGesq-UQ'
key = input('Insert your own key: ')
video = input('Insert the video URL: ')
videoId = video.split('=')
videoId = videoId[1]

print('Downloading...')

# COMMENTS
## Comment parents in a list
nextToken = None
snippet = []
while True:
    response = ct.callAPI(key, videoId, 'snippet', nextToken)
    
    for value in response.json()['items']:
        snippet.append(value['snippet']['topLevelComment']['snippet'])
    
    nextToken = response.json()['nextPageToken'] if 'nextPageToken' in response.json().keys() else None

    if not nextToken:
        break

## List of comment parents in a Data frame
df = pd.DataFrame(snippet)

## Saving in a CSV
df.to_csv(r'./comments_parent.csv', encoding='utf-8-sig')
print('The table "comments_parents.csv" is saved.')

# REPLIES
## Comment replies in a list
nextToken = None
replies = []
while True:
    response = ct.callAPI(key, videoId, 'replies', nextToken)
    for value in response.json()['items']:
        if 'replies' in value.keys():
            for comment in value['replies']['comments']:
                replies.append(comment['snippet'])
    
    nextToken = response.json()['nextPageToken'] if 'nextPageToken' in response.json().keys() else None

    if not nextToken:
        break

## List of comment replies in a Data frame
df = pd.DataFrame(replies)

## Saving in a CSV
df.to_csv(r'./comments_replies.csv', encoding='utf-8-sig')
print('The table "comments_replies.csv" is saved.')