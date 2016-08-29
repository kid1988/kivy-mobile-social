from .vk_api import *
from pyobjus import protocol


class Delegate(object):
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


class UiDelegate(object):
    @protocol('VKSdkUIDelegate')
    def vkSdkShouldPresentViewController_(self, controller):
        delegate = VkApi.ui_delegate

        delegate.presentController_(controller,)