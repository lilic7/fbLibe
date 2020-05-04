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
            print(response.text)

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

    def get_stream_key(self, stream_url):
        return stream_url.split("/rtmp/")[1]


