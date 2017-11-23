# coding:utf-8
import os
# from jishu_dict import tv_dict
# import time

path = "D:/Work_Liu/html5_video/static/media/".encode('gbk')
file_list = os.listdir(path)
# file_list = file_list1.decode('gbk').encode('utf-8')
print(file_list)


def mactch_name(words):
    names = []
    for i in file_list:
        i = i.decode('gbk').encode('utf-8')
        if i in words:
            names.append(i)
    if names != [] and names is not None:
        # print 'name', names[-1]
        return names[-1]


def filter_tv_name(data):
    matched_name = mactch_name(data)
    # print mactch_name
    if not matched_name:
        # print 'error error'
        return 'error'
    else:
        # print mactch_name
        return matched_name

# def run_name():
# while True:
#     data = raw_input('输入: ')
#     test_tv_name(data)
