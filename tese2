# -*- coding: UTF-8 -*-
#创建两个线程，使用共享全局变量isshow
import  time
import  threading

isshow = 0
def show():
    global  isshow
    while True:
        while isshow == 1:
            print("线程1进行中")
            time.sleep(.1)
def is_show():
    global isshow
    while True:
        miao = int(time.time())
        if miao % 2 == 0 :
            isshow = 0
            print("线程2来了" + str(miao))
            time.sleep(.1)
        else:
            isshow = 1

if __name__ == '__main__':
    # lock = threading.RLock()
    t1 = threading.Thread(target=is_show)
    t1.start()
    t2 = threading.Thread(target=show)
    t2.start()
