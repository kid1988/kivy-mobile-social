# coding=utf-8
from kivy.network.urlrequest import UrlRequest


class FbApi:
    DELIMITER = '/'
    URL = 'https://graph.facebook.com/'

    _id = 0
    _secret = None
    _token = None

    @property
    def token(self):
        return self._token

    def __init__(self, app_id='', **kwargs):
        self.app_id = app_id
        self.auth()
        self.callback = None

    def auth(self):
        pass

    def request(self, url, callback, params):
        print('request!!!')
        self.callback = callback
        params['access_token'] = self._token
        args = self.create_args_string(params)
        url = self.URL + '/'.join(url) + '/?' + args

        UrlRequest(url=url, on_success=self.on_success, on_error=self.on_error,
                   on_failure=self.on_error)

    def on_success(self, req, resp):
        print('response!', resp)
        if self.callback is not None:
            self.callback(resp)

    def on_error(self, req, err):
        print('response error!', type(err))

    def create_args_string(self, params):
        args = []
        if params:
            for k, v in params.items():
                args.append('='.join([k,v]))

        return '&'.join(args)