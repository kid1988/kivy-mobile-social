# coding=utf-8
from importlib import import_module
from plyer.utils import platform

module = 'facebook.{}.fb_api'.format(platform)
try:
    fb_api = import_module(module)
except ImportError as e:
    fb_api = import_module('facebook.default.fb_api')
