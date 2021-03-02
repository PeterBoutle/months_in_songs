
import lyricsgenius



months = ["January","February","March","April","May","June","July","August","September","November","December"]
scores = {"January":0,"February":0,"March":0,"April":0,"May":0,"June":0,"July":0,"August":0,"September":0,"November":0,"December":0}

artists = ["Bob Dylan", "Fairport Convention", "Pete Seeger","Pentangle","Bert Jansch","Steeleye Span","Sandy Denny","Shirley Collins","Davy Graham","Martin Carthy"]

client_access_token = "put token here"

genius = lyricsgenius.Genius(client_access_token)
genius.verbose = True


for artist in artists:

    matched_artist = genius.search_artist(artist, sort="popularity",max_songs=100)

    for song in matched_artist.songs:
        lyric = song.lyrics
        lyric_set = set(lyric.split())
        matches = set(months) & lyric_set
        if len(matches) >0:
            for match in matches:
                scores[match] += 1





print(scores)

