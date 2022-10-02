import lyricsgenius as lg # https://github.com/johnwmillr/LyricsGenius


file = open("lyrics_1.txt", "w")  # File to write lyrics to
genius = lg.Genius('Client_Access_Token_Goes_Here',  # Client access token from Genius Client API page
                             skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                             remove_section_headers=True)

artists = ['Akon', 'Neha Kakkar', 'Justin Bieber']


def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in arr
    c = 0  # Counter
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))  # Deliminator
            c += 1
            print(f"Songs grabbed:{len(s)}")
        except:  #  Broad catch which will give us the name of artist and song that threw the exception
            print(f"some exception at {name}: {c}")


get_lyrics(artists, 3)