# coding=utf-8
import sys

from pyobjus import autoclass
from pyobjus import protocol

from ..default import vk_api
from delegates import Delegate, UiDelegate

VKSdk = autoclass('VKSdk')

OurVK = autoclass('OurVk')
VKUIDelegate = autoclass('VKUIDelegate')


class VkApi(vk_api.VkApi):
    APP_ID = 5552065

    def __init__(self, app_id):
        self.APP_ID = app_id
        self.delegate = Delegate()
        self.ui_delegate = UiDelegate()

        self.vk = OurVK.alloc().init()
        self.vk.setDelegate_(self.delegate)
        self.vk.setUiDelegate_(self.ui_delegate)

        self.auth()
        VkApi.instance = self

    @staticmethod
    def get_instance():
        return VkApi.instance

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

    @protocol('VKSdkDelegate')
    def vkSdkAccessTokenUpdated_oldToken_(self, new_token, old_token):
        vk_api = VkApi.get_instance()
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
