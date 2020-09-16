import functions.youtube_api as yb
import functions.search as search

# TESTE
key = 'AIzaSyDazwNBxt816APtEYPQl5jAGg0YTRwQyPM'
channelId = 'UCTHuWvQ21wbpYtZz92EUVjA'

videos = yb.videosIds(key, channelId)
videosIds = yb.youtubeComments(key, videos)