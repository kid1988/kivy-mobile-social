# coding=utf-8
import json

from vkontakte import vk_api
from facebook import fb_api


class SocialApi:
    """
        API for accessing to social network
    """
    _social_net = {
        'vkontakte': {'obj': vk_api.VkApi, 'instance': None},
        'facebook': {'obj': fb_api.FbApi, 'instance': None}
    }

    def __init__(self, social_net):
        if self._social_net[social_net]['instance'] is None:
            Social = self._social_net[social_net]['obj']
            self._social_net[social_net]['instance'] = Social()

        self.api = self._social_net[social_net]['instance']

    def __getattr__(self, item):
        return GenerateRequest(self, [item])

    def request(self, method, **kwargs):
        # url = self.api.URL + method
        response = self.api.request(method, kwargs)
        print('method', method, kwargs)
        return json.loads(response.text)


class GenerateRequest:
    def __init__(self, api_instance, method=[]):
        self._api_instance = api_instance
        self._method = method

    def __getattr__(self, method_name):
        self._method.append(method_name)
        return GenerateRequest(self._api_instance, self._method)

    def __call__(self, **kwargs):
        return self._api_instance.request(self._method, **kwargs)


a = SocialApi(social_net='vkontakte')
res = a.users.get(user_ids='322883', fields=['sex', 'online'])
print('result', res)
# b = SocialApi(social_net='facebook')
# res = b.me()
# print('result', res)


