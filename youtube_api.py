import CommentThreads as ct
import csv
import pandas as pd

key = 'AIzaSyD2rSHON0Moknt9H5Jegf06MggNv64PhqU'
videoId = 'D_xftS6ydXQ'

# Comment parents in a list
nextToken = None
snippet = []
while True:
    response = ct.callAPI(key, videoId, 'snippet', nextToken)
    
    for value in response.json()['items']:
        snippet.append(value['snippet']['topLevelComment']['snippet'])
    
    nextToken = response.json()['nextPageToken'] if 'nextPageToken' in response.json().keys() else None

    if not nextToken:
        break

# List of comment parents in a Data frame
df = pd.DataFrame(snippet)

print(df)
print(df.keys())

# Saving in a CSV
df.to_csv(r'./comments_parent.csv', encoding='utf-8-sig')

# Comment replies in a list
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

# List of comment replies in a Data frame
df = pd.DataFrame(replies)

print(df)
print(df.keys())

# Saving in a CSV
df.to_csv(r'./comments_replies.csv', encoding='utf-8-sig')