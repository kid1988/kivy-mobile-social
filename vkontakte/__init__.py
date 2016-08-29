# coding=utf-8
from importlib import import_module
from plyer.utils import platform

module = 'vkontakte.{}.vk_api'.format(platform)
print(module)
try:
    vk_api = import_module(module)
except ImportError as e:
    print("error", str(e))
    vk_api = import_module('vkontakte.default.vk_api')

