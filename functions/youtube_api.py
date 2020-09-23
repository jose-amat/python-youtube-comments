# Importing packages
import functions.CommentThreads as ct
import functions.search as search
import functions.videos as videos
import functions.playlistItems as plist
import pandas as pd


# Returns the videos ids in a Data Frame
def videosIds(key, Id, order, isChannel):

    if isChannel:
        # COMMENTS
        ## Pandas data frame
        df = search.videosDataFrame(key, Id, order) # DataFrame with 21 rows
        df = search.dropColumns(df) # Dropping some columns
        df = search.dropRows(df) # Dropping missing id values
        search.dataFrameToCSV(df)
        print(df)
        return df
    else:
        df = plist.videosDataFrame(key, Id)
        plist.dataFrameToCSV(df)
        print(df)
        return df


# Save the DataFrame as CSV
def youtubeComments(key, videosIds):

    ## Comment Parents
    df = pd.DataFrame()
    for index, row in videosIds.iterrows():
        data = ct.parentsDataFrame(key, row['videoId'])
        df = pd.concat([data, df])
    
    ct.dataFrameToCSV(df, True)
    
    ## Comment Replies
    df = pd.DataFrame()
    for index, row in videosIds.iterrows():
        data = ct.repliesDataFrame(key, row['videoId'])
        df = pd.concat([data, df])

    ct.dataFrameToCSV(df, False)

def commentsByChannel(key, channelId, order):
    videoId = videosIds(key, channelId, order, True)

    youtubeComments(key, videoId)

def commentsByPlaylist(key, playlistId):
    videoId = videosIds(key, playlistId, None, False)

    youtubeComments(key, videoId)