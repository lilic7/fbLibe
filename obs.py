import json
import os


class Obs:
    def __init__(self, profile="FbLive"):
        user_profile = os.getlogin()
        self.path = f'C:\\Users\\{user_profile}\\AppData\\Roaming\\obs-studio\\basic\\profiles\\FbLive'
        self.obs_link = os.path.dirname(__file__) + '\\data\\obs.lnk'
        self.profile = profile
        self.settings = self.read_settings()

    def read_settings(self):
        with open(f'{self.path}\\service.json') as settings_data:
            return json.load(settings_data)

    def write_settings(self):
        with open(f'{self.path}\\service.json', 'w') as settings_file:
            json.dump(self.settings, settings_file)

    def change_key(self, key):
        if key:
            self.settings['settings']['key'] = key
        else:
            print("No key defined")
        self.write_settings()

    def start_live(self):
        os.system(f"start {self.obs_link} --profile \"{self.profile}\" --startstreaming --minimize-to-tray")