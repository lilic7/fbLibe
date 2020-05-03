import json
import unittest
from fbLive.settings import FbSettings


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        filename = '../fbLive/settings.json'
        self.fbSettings = FbSettings()
        with open(filename) as settings:
            self.data = json.load(settings)

    def test_read_json(self):
        self.assertEqual(self.data, self.fbSettings.read_json())

    def test_get_user_token(self):
        user_access_token = self.data['user_access_token']
        fb_user_access_token = self.fbSettings.get_user_token()
        self.assertEqual(user_access_token, fb_user_access_token)

    def test_change_user_token(self):
        new_user_token = '123abc'
        self.fbSettings.change_user_token(new_user_token)
        result = self.fbSettings.get_user_token()
        self.assertEqual(new_user_token, result)

    def test_get_pages(self):
        pages = self.data['pages']
        fb_pages = self.fbSettings.get_pages()
        self.assertEqual(pages, fb_pages)

    def test_get_page_valid_name(self):
        page = self.data['pages'][1]
        fb_page = self.fbSettings.get_page(page['page_name'])
        self.assertEqual(page, fb_page)
    
    def test_get_page_invalid_name(self):
        page_name = 'Page_not_exist'
        fb_page = self.fbSettings.get_page(page_name)
        self.assertFalse(fb_page)



if __name__ == '__main__':
    unittest.main()
