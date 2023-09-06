import urllib
import json
import requests
import time

from random import *


TOKEN = "6398049872:AAGwlITpxsj9uuS7y4AJbzGuA-xJo7P7ICA"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

words = ["apple", "banana", "orange"]
gamelist = {}


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js