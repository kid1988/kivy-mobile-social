# coding=utf-8
from importlib import import_module
from plyer.utils import platform

module = 'vkontakte.{}.vk_api'.format(platform)
try:
    vk_api = import_module(module)
except ImportError as e:
    vk_api = import_module('vkontakte.default.vk_api')

