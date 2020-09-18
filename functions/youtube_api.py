# Importing packages
import functions.CommentThreads as ct
import functions.search as search
import pandas as pd


# Returns the videos ids in a Data Frame
def videosIds(key, channelId):

    # COMMENTS
    ## Pandas data frame
    df = search.videosDataFrame(key, channelId) # DataFrame with 21 rows
    df = search.dropColumns(df) # Dropping some columns
    df = search.dropRows(df) # Dropping missing id values
    search.dataFrameToCSV(df)
    print('The table "videos_ids.csv" is saved.')
    
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

def commentsPerChannel(key, channelId):
    videoId = videosIds(key, channelId)

    youtubeComments(key, videoId)
    print("FINISHED!")