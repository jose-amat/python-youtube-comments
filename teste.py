import functions.youtube_api as yb

key = 'AIzaSyDazwNBxt816APtEYPQl5jAGg0YTRwQyPM'
playlist = 'PLlBw3F15IXehbaG16XZ0eokoNWDKjFzQ-'

videos = yb.commentsByPlaylist(key, playlist)