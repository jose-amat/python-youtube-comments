# Importing packages
import functions.CommentThreads as ct


def youtubeComments(key, video):
    videoId = video.split('=')
    videoId = videoId[1]

    # COMMENTS
    ## Pandas data frame
    df = ct.parentsDataFrame(key, videoId)

    ## Saving in a CSV
    ct.dataFrameToCSV(df, True)

    # REPLIES
    ## Pandas data frame
    df = ct.repliesDataFrame(key, videoId)

    ## Saving in a CSV
    ct.dataFrameToCSV(df, False)    

    print("Done!")