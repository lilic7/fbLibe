import json
import requests

from fbLive.settings import FbSettings


class FbLive:
    def __init__(self, page_name):
        self.settings = FbSettings()
        self.page = self.settings.get_page(page_name)
        self.live_data = {}

    def get_active_page(self):
        return self.page

    def create_live(self):
        query = "https://graph.facebook.com/{}/live_videos?status=LIVE_NOW&access_token={}".format(
            self.page['id'],
            self.page['access_token']
        )
        try:
            response = requests.post(query)
            self.live_data = json.loads(response.text)
            return self.get_stream_key(self.live_data['stream_url'])
        except:
            print("Create live", response.text)

    def end_live(self):
        query = "https://graph.facebook.com/{}?" \
                "end_live_video=true&" \
                "access_token={}".format(
            self.live_data['id'],
            self.page['access_token']
        )
        try:
            response = requests.post(query)
            return json.loads(response.text)
        except:
            print(response.text)

    @staticmethod
    def get_stream_key(stream_url):
        return stream_url.split("/rtmp/")[1]

    def get_stream_status(self):
        query = "https://graph.facebook.com/{}?" \
                "fields=ingest_streams&access_token={}".format(
            self.live_data['id'],
            self.page['access_token']
        )
        try:
            print(f"{self.live_data} \n {self.page['access_token']}")
            response = requests.get(query)
            data = json.loads(response.text)
            video_width = data['ingest_streams'][0]['stream_health']['video_width']
            video_height = data['ingest_streams'][0]['stream_health']['video_height']
            video_framerate = data['ingest_streams'][0]['stream_health']['video_framerate']
            video_bitrate = data['ingest_streams'][0]['stream_health']['video_bitrate'] / 1000000
            audio_bitrate = data['ingest_streams'][0]['stream_health']['audio_bitrate'] / 1000
            # dash_url = data['ingest_streams'][0]['dash_preview_url']
            return {
                # "dash_url": dash_url,
                "size": f"{video_width}x{video_height}",
                "framerate": str(round(video_framerate)),
                "v_bitrate": str(round(video_bitrate, 3)),
                "a_bitrate": str(round(audio_bitrate, 3))
            }
        except:
            print("Error: "+response.text)

