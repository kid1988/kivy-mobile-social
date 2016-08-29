# coding=utf-8
from kivy.network.urlrequest import UrlRequest


class VkApi(object):
    APP_ID = 5552065

    _ui_delegate = None
    _vk_token = None
    _user_id = None
    _auth_done = None
    instance = None
    DELIMITER = '.'
    URL = 'https://api.vk.com/method/'

    _token = None

    @property
    def token(self):
        return self._token

    def request(self, url, callback,  params):
        print('request!!!')
        self.callback = callback
        params['access_token'] = self._token

        url = self.URL + '/'.join(url)

        UrlRequest(url=url, on_success=self.on_success, on_error=self.on_error,
                   on_failure=self.on_error, req_body=params)

    def on_success(self, req, resp):
        print('response!', resp)
        if self.callback is not None:
            self.callback(resp)

    def on_error(self, req, err):
        print('response error!', type(err))