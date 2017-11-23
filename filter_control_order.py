# coding:utf-8
order_dict = {
    '播放': 'play',
    '暂停': 'pause',
    '快进': 'forward',
    '前进': 'forward',
    '快退': 'back',
    '后退': 'back',
    '倒退': 'back',
    '全屏': 'full',
    '退出全屏': 'exitfull',
    '加声音': 'voiceup',
    '加音量': 'voiceup',
    '提高音量': 'voiceup',
    '提升音量': 'voiceup',
    '降低音量': 'voicedown',
    '减小音量': 'voicedown',
    '减少音量': 'voicedown',
    '减声音': 'voicedown',
    '减音量': 'voicedown',
}


def mactch_control_order(words):
    or_list = []
    for i in order_dict.keys():
        if i in words:
            or_list.append(i)
    # print(or_list)
    if len(or_list) >= 1:
        return order_dict[or_list[-1]]
    else:
        pass


# while True:
#     words = raw_input('uuru: ')
#     print mactch_name(words)