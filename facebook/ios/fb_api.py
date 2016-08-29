from collections import deque
from pyobjus import autoclass
from pyobjus import protocol

from ..default import fb_api

FbAuth = autoclass("FbAuth")


class FbApi(fb_api.FbApi):
    generator = None
    request_queue = deque()

    def __init__(self, app_id='', **kwargs):
        self.app_id = app_id
        self.auth()

    def auth(self):
        fb_auth = FbAuth.alloc().init()
        # delegate = Delegate()
        fb_auth.setDelegate_(self)

        fb_auth.login()


    @protocol("FbDelegate")
    def getToken_(self, token):
        token = token.UTF8String()
        self._token = token
        if self.request_queue:
            for request in self.request_queue:
                request()
        print('delegate', token)


# class Delegate(object):
#     @protocol("FbDelegate")
#     def getToken_(self, token):
#         print('delegate', token.UTF8String())