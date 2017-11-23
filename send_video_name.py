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
    "tip": 'video_name',
    "name": '',
    "num": '',
    "order": 0
}


def send_video_name(name, num):
    data['name'] = name
    # print 'name', name
    data['num'] = num
    # print 'num', num
    order1 = json.dumps(data)
    params['content'] = order1
    req = requests.post(url, data=params)
