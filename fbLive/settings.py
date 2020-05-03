import json


class FbSettings:
    def __init__(self):
        self.settings = self.read_json()

    def read_json(self):
        filename = './fbLive/settings.json'
        try:
            with open(filename) as settings:
                return json.load(settings)
        except FileNotFoundError:
            print(f"File '{filename}' does not exists")

    def write_to_json(self):
        filename = './settings.json'
        try:
            with open(filename, "w") as settings:
                json.dump(self.settings, settings)
        except FileNotFoundError:
            print(f"File '{filename}' does not exists")

    def change_user_token(self, token):
        self.settings["user_access_token"] = token
        self.write_to_json()

    def get_user_token(self):
        return self.settings["user_access_token"]

    def get_app_data(self):
        return {"app_id": self.settings['app_id'], "app_secret": self.settings["app_secret"]}

    def get_user_id(self):
        return self.settings["user_id"]

    def get_pages(self):
        return self.settings['pages']

    def get_page(self, page_name):
        items = list(filter(lambda item: item["name"] == page_name, self.settings['pages']))
        if len(items):
            return items[0]
        return False

    def save_pages_data(self, pages):
        pages_to_save = []
        for page in self.settings["pages"]:
            page_name = page["name"]
            api_page = filter(lambda item: item["name"] == page_name, pages)
            pages_to_save.append(list(api_page)[0])
        self.settings['pages'] = pages_to_save
        self.write_to_json()
