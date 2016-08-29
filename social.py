# coding=utf-8
"""
Module provided API for social networks vkontakte and facebook.

How to use:
    - Create instance:
        social = SocialApi(social_net="facebook")
    As argument use name of social network - "facebook" or "vkontakte"
    - Use API:
        example for vkontakte:
            result = social.friends.get(user_id='"1", fields=['nickname'])
        Return list of friends with nicknames for user "1".
        "friends.get" - is vkontakte method. Use other methods like this. As arguments for
        function use method arguments from vkontakte API.

        exampla for facebook:
            result = social.me()
        Return information about current user.
        "me" - is node from graph API facebook.
"""
import json

from functools import partial
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

    def __init__(self, social_net, **kwargs):
        if self._social_net[social_net]['instance'] is None:
            Social = self._social_net[social_net]['obj']
            self._social_net[social_net]['instance'] = Social(**kwargs)

        self.api = self._social_net[social_net]['instance']

    def __getattr__(self, item):
        return GenerateRequest(self, [item])

    def request(self, method, callback, **kwargs):

        if self.api.token is not None:
            self.api.request(method, callback, kwargs)
        else:
            request = partial(self.api.request, method, callback, kwargs)
            self.api.request_queue.append(request)


class GenerateRequest:
    def __init__(self, api_instance, method=[]):
        self._api_instance = api_instance
        self._method = method

    def __getattr__(self, method_name):
        self._method.append(method_name)
        return GenerateRequest(self._api_instance, self._method)

    def __call__(self, callback, **kwargs):
        return self._api_instance.request(self._method, callback, **kwargs)




