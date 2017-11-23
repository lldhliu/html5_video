# coding:utf-8
from video_num_dict import tv_dict


def filter_tv_num(message):
    matched_words = mactch_words(message)
    if not matched_words:
        # print('no such a video num')
        return False
    else:
        video_val = tv_dict[matched_words]
        # print(video_val)
        return video_val


def mactch_words(words):
    nums = []
    for i in tv_dict.keys():
        if i in words:
            nums.append(i)
    # print 'numsss: ', nums
    if nums != [] and nums is not None:
        # print nums
        print max(nums)
        return max(nums)

# words = raw_input('uuru: ')
# print filter_tv_num(words)
