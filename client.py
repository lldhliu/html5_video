# coding:utf-8
import socket

# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 192.168.0.103
addr = ('127.0.0.1', 8500)
# 接受多次数据
while True:

    data = raw_input('请输入要发送的数据：')
    # 如果为'quit',则退出
    if data == 'quit':
        break
    # 发送数据
    s.sendto(data, addr)
    # 打印接收到的数据
    b = s.recv(1024)
    # print type(b)

# 关闭socket
s.close()
