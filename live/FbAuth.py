import json
import requests
from live.FbSettings import FbSettings


class FbAuth:
    def __init__(self):
        self.settings = FbSettings()

    def get_pages(self):
        query = "https://graph.facebook.com/{}/accounts?" \
                "fields=name,access_token&" \
                "access_token={}".format(
            self.settings.get_user_id(),
            self.settings.get_user_token()
        )
        try:
            response = requests.get(query)
            pages = json.loads(response.text)['data']
            self.settings.save_pages_data(pages)
        except:
            print(response.text)

    def change_user_token(self):
        app_data = self.settings.get_app_data()
        query = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token" \
                "&client_id={}" \
                "&client_secret={}" \
                "&fb_exchange_token={}".format(
            app_data["app_id"],
            app_data['app_secret'],
            self.settings.get_user_token()
        )
        try:
            response = requests.get(query)
            token = json.loads(response.text)['access_token']
            self.settings.change_user_token(token)
        except:
            print(response.text)
