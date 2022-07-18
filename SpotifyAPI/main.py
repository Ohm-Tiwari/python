import json

import requests
from Secondary import spotify_user_id, release_radar_ID
from datetime import date
from refresh import Refresh

class Save_Songs:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""
        self.release_radar_ID = release_radar_ID
        self.tracks = ""
        self.new_playlist_ID = ""

    def find_songs(self):
        #Loops through playlist and adds to a list

        print("Finding songs in release rader")

        query = "https://api.spotify.com/v1/playlists/{37i9dQZEVXbxuLCT3EIXL3}/tracks".format(release_radar_ID)

        response = requests.get(query,
                            headers={"Content-Type": "application/json",
                                "Authorization": "Bearer {}".format(self.spotify_token)})

        response_json = response.json()
        
        print(response)

        for i in response_json["items"]:
            self.tracks += (i["track"]["uri"] + ",")
        self.tracks = self.tracks[:-1]

        self.add_to_playlist()

    def create_playlist(self):
        #Creates a new playlist
        print("Attemping to create playlist")
        today = date.today()

        todayFormatted = today.strftime("%m/%d/%Y")

        query = "https://api.spotify.com/v1/users/{}/playlist".format(spotify_user_id)
        
        request_body = json.dumps({
            "name": todayFormatted + "Release Radar", "description": "Release Radar for the week in the title :)", "public": True
        })

        response = requests.post(query, data=request_body, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })
        
        response_json = response.json()
        return response_json["id"]

    def add_to_playlist(self):
        #adds songs to the playlist
        print("adding songs")

        self.new_playlist_ID = self.create_playlist()

        query = "https://spotify.com/v1/playlists/{}/tracks".format(self.new_playlist_ID, self.tracks)

        response = requests.post(query,  headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.spotify_token)
        })

        print(response.json)

    def call_refresh(self):

        print("Refreshing token")


        refreshCaller = Refresh()

        self.spotify_token = refreshCaller.refresh()

        self.find_songs()

a = Save_Songs()
a.call_refresh()



