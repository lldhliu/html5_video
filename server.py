# coding:utf-8
import socket
import time
from filter_video_name import filter_tv_name
from filter_video_num import filter_tv_num
from send_video_name import send_video_name
from send_control_order import send_order
from filter_control_order import mactch_control_order
# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('0.0.0.0', 8500)
s.bind(address)
print('Server is running...')


# 服务器端处理逻辑
while True:
    # 接受其数据
    data, addr = s.recvfrom(1024)
    print(data)
    if data[:3] == 'A01':
        video_name = filter_tv_name(data)
        # print 'video_name', video_name
        # print (data[-16:])
        video_num = filter_tv_num(data[-16:])
        # print 'video_num', video_num
        if video_name != 'error':
            # send_video_name(video_name, video_num)
            # s.sendto('B01播放成功', addr)
            if video_num:
                send_video_name(video_name, video_num)
                s.sendto('B01播放成功', addr)
            else:
                s.sendto('B02还没更新到这一集,换一集吧', addr)
        else:
            s.sendto('B02没有找到你要播放的电视剧,换一个吧', addr)
    elif data[:3] == 'A02':
        order = mactch_control_order(data)
        # print 'order', order
        send_order(order)
        # s.sendto('B01成功执行你的命令', addr)
    # 延迟
    time.sleep(1)

# 关闭连接
s.close()
