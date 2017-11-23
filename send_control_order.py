# coding:utf-8
import requests
import json


params = {
    'appkey': 'BC-27c35f3b5d294e888a4fa31c72e0a47b',
    'channel': 'video_channel',
    'content': '666666666666'
}

url = 'https://rest-hangzhou.goeasy.io/publish'
data = {
    "tip": 'video_order',
    "name": 0,
    "num": 0,
    "order": '播放'
}


def send_order(order):
    data['order'] = order
    order1 = json.dumps(data)
    params['content'] = order1
    req = requests.post(url, data=params)
