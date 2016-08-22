# coding=utf-8
import requests


class VkApi(object):
    APP_ID = 5552065

    _ui_delegate = None
    _vk_token = None
    _user_id = None
    _auth_done = None
    instance = None
    DELIMITER = '.'
    URL = 'https://api.vk.com/method/'

    def request(self, url, params):
        url = self.URL + '.'.join(url)
        print(url,params)
        response = requests.request('POST', url=url, params=params)
        return response