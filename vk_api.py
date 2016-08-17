from kivy.network.urlrequest import UrlRequest
from pyobjus import autoclass, protocol, objc_str
from pyobjus.protocols import protocols
from pyobjus.dylib_manager import load_framework, INCLUDE

import sys
import time
import vk

path = ''
for p in sys.path:
    if p.endswith('vk-api.app'):
        path = p
        break

load_framework(path + '/Frameworks/VKSdkFramework.framework')
load_framework('/System/Library/Frameworks/UIKit.framework')

NSString = autoclass('NSString')
NSArray = autoclass("NSArray")
NSObject = autoclass("NSObject")
VKSdk = autoclass('VKSdk')

OurVK = autoclass('OurVk')
VKUIDelegate = autoclass('VKUIDelegate')


class VkIosApi(object):
    APP_ID = 5552065

    _ui_delegate = None
    _vk_token = None
    _user_id = None
    _auth_done = None
    instance = None

    @property
    def auth_done(self):
        return self._auth_done

    @auth_done.setter
    def auth_done(self, value):
        self._auth_done= value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def vk_token(self):
        return self._vk_token

    @vk_token.setter
    def vk_token(self, value):
        self._vk_token = value

    @property
    def ui_delegate(self):
        return self._ui_delegate

    @ui_delegate.setter
    def ui_delegate(self, value):
        self._ui_delegate = value

    def __init__(self):

        self.delegate = Delegate()
        self.ui_delegate = UiDelegate()

        self.vk = OurVK.alloc().init()
        self.vk.setDelegate_(self.delegate)
        self.vk.setUiDelegate_(self.ui_delegate)

        self.auth()
        VkIosApi.instance = self

    @staticmethod
    def get_instance():
        return VkIosApi.instance

    def auth(self):
        self.vk.vkSession_(self.APP_ID)

        self.auth_done = self.use()
        self.auth_done.next()

    def use(self):
        while True:
            auth_done = yield

            if auth_done:
                print('coroutine', self.vk_token)
                self.user_id = self.vk.getUserId().UTF8String()
                print('userid', self.user_id)
                session = vk.Session(access_token=self.vk_token)
                self.vk_api = vk.API(session, lang='ru')
                try:
                    users = self.vk_api.users.get(user_ids=self.user_id)
                    print('users', users)
                except BaseException as e:
                    print('zapros fail: {}'.format(str(e)))


class Delegate(object):
    @protocol('VKSdkDelegate')
    def vkSdkAccessTokenUpdated_oldToken_(self, new_token, old_token):
        vk_api = VkIosApi.get_instance()
        old_token = old_token.UTF8String()

        if old_token is not None:
            new_token = new_token.UTF8String()

            if vk_api.vk_token is None or old_token != new_token:
                vk_api.vk_token = new_token

                coroutine = vk_api.auth_done
                coroutine.send(True)

        # print('update token', new_token, old_token)

    @protocol('VKSdkDelegate')
    def vkSdkAuthorizationStateUpdatedWithResult_(self, token):
        self.vk_api.vk_token = token.UTF8String()
        print('update with result')

    @protocol('VKSdkDelegate')
    def vkSdkAccessAuthorizationFinishedWithResult_(self, token):
        self.vk_api.vk_token = token.UTF8String()
        print('finish with result')

    @protocol('VKSdkDelegate')
    def vkSdkTokenHasExpired_(self, *args):
        print('expired')


class UiDelegate(object):
    @protocol('VKSdkUIDelegate')
    def vkSdkShouldPresentViewController_(self, controller):
        delegate = VkIosApi.ui_delegate

        delegate.presentController_(controller, )
