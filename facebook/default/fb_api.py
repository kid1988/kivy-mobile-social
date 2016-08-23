# coding=utf-8
import requests


class FbApi:
    DELIMITER = '/'
    URL = 'https://graph.facebook.com/'
    URL_AUTH = 'https://www.facebook.com/dialog/oauth'

    _id = 0
    _secret = None
    _token = None

    def __init__(self, app_id='', **kwargs):
        self.app_id = app_id
        self.auth(**kwargs)

    def auth(self, **kwargs):
        pass