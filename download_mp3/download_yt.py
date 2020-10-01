import apiclient
import os
import config


def download_song(song):
    """
    : Download the song after querying it from YT db.
    : Null check at the main itself.
    : param song: song (string) provided by the user.
    : return: Nothing. Saves the audio file in the present working directory.
    """
    api_key = config.api_key
    youtube = apiclient.discovery.build("youtube", "v3", developerKey=api_key)
    req = youtube.search().list(q=song, part="snippet", type="video")
    res = req.execute()
    video_id = res["items"][0]["id"]["videoId"]
    os.system(
        'youtube-dl -x --audio-format mp3 --audio-quality \
        0 --output "%(title)s.%(ext)s" '
        "https://www.youtube.com/watch?v=" + video_id
    )
    print("Song downloaded..yay!!")
    print("------------------------------------------")


# Driver code
if __name__ == "__main__":
    while True:
        print("Press n(N) if you want to quit!")
        try:
            song = input("Please enter song / artist: ")
            if len(song) < 2:
                print("Thanks for using this!")
                break
            download_song(song)
        except Exception:
            break
