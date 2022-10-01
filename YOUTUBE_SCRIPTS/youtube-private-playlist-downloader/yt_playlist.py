""" To access your private youtube playlist.

NEEDED 'client_secret_file.json' for your google account.
        follow instructions in https://developers.google.com/youtube/v3/quickstart/python#step_1_set_up_your_project_and_credentials  # noqa: E501
        to download your client secret file.
"""

import sys
import os

import google_auth_oauthlib.flow  # pip install google_auth_oauthlib
import googleapiclient.discovery  # pip install google-api-python-client
import googleapiclient.errors

import pafy  # pip install pafy youtube-dl


class YT:

    def __init__(self, p_client_secrets_file: str):
        """
        Args:
            p_client_secrets_file : string = path of the client_secret_*.json file
        """
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = p_client_secrets_file
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]  # For _get_content
        scopes += ["https://www.googleapis.com/auth/youtube.force-ssl"]  # For _delete_playlist_items

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes
        )
        credentials = flow.run_console()

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials
        )
        self.youtube = youtube

    def _get_content(self, playlistId: str, n: int = 50):
        """To get contentDetails from playlistId ( for Private Playlist )
        Args:
            playlistId : str = Unique playlistId
            n : int = number of videos to download
        Returns : dict = response json
        """
        request = self.youtube.playlistItems().list(
            part="contentDetails", playlistId=playlistId, maxResults=n
        )
        response = request.execute()
        return response

    def get_video_ids(self, playlistId: str, n: int = 50):
        """To get video ids.
        Args:
            playlistId : str = Unique playlistId
            n : int = number of videos to download
        Return : list(str) = list of ids of videos in Playlist
        """
        response = self._get_content(playlistId, n)
        IDs = list()
        for item in response["items"]:
            IDs.append(item["contentDetails"]["videoId"])
        return IDs

    def get_playlist_item_ids(self, playlistId: str, n: int = 50):
        """To get playlist item ids.
        This id is used for removing a video from playlist.
        Args:
            playlistId : str = Unique playlistId
            n : int = number of videos to download
        Return : list(str) = list of ids of items (videos) in Playlist
        """
        response = self._get_content(playlistId, n)
        IDs = list()
        for item in response["items"]:
            IDs.append(item["id"])
        return IDs

    @staticmethod
    def _download(video_ids):
        """To download the videos.
        Args:
            video_ids : list(str) = List of video ids has to be downloaded
        """
        for i, video_id in enumerate(video_ids):
            url = "https://www.youtube.com/watch?v=" + video_id
            File = pafy.new(url)
            video_file = File.getbest()
            size = round(video_file.get_filesize() / 2 ** 20, 2)
            print("\n" + str(i + 1), video_file.filename, ":", str(size) + "MB")
            try:
                video_file.download()
            except KeyboardInterrupt:
                break
            except Exception:
                print(i + 1, sys.exc_info())

    def download(self, playlistId: str, n: int = 50):
        """To download the videos.
        Args:
            playlistId : str = Unique playlistId
            n : int = number of videos to download
        """
        video_ids = self.get_video_ids(playlistId, n)
        self._download(video_ids)

    def _delete_playlist_items(self, ids):
        """To remove videos from playlist
        Args:
            ids : list(str) = list of ids of playlistItems has to be deleted.
        """
        for i, id_ in enumerate(ids):
            try:
                request = self.youtube.playlistItems().delete(id=id_)
                response = request.execute()
            except KeyboardInterrupt:
                break
            except Exception:
                print(i + 1, sys.exc_info())
            else:
                print(i + 1, response)

    def delete(self, playlistId: str, n: int = 50):
        """To download the videos.
        Args:
            playlistId : str = Unique playlistId
            n : int = number of videos to download
        """
        playlist_ids = self.get_playlist_item_ids(playlistId, n)
        self._delete_playlist_items(playlist_ids)


if __name__ == "__main__":
    ytpl = YT(input("Enter path of client_secret_.*.json > "))
    PLid = input("Enter PlaylistID > ")
    n = int(input("How many videos you want to download? >> "))
    ytpl.download(PLid, n)

    if input("\n\nWould you like to delete these videos from playlist? [y/N] > ").lower() == "y":
        ytpl.delete(PLid, n)
