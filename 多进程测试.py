# -*- coding: UTF-8 -*-
#创建两个进程程，共享变量使用 变量名.Value("i",0)，也可以使用元组 变量名.Array('i', [1, 2, 3, 4])共享多个变量
import  time
import multiprocessing as mp
def show(isshow):
    while True:
        while isshow.value == 1:
            print("进程1进行中")
            # time.sleep(.1)
def is_show(isshow):
    while True:
        miao = int(time.time())
        if miao % 2 == 0 :
            isshow.value = 0
            print("进程2来了" + str(miao))
            # time.sleep(.1)
        else:
            isshow.value = 1

if __name__ == '__main__':
    isshow = mp.Value("i",0)  #初始赋值为0
    m1 = mp.Process(target=show,args=(isshow,))
    m1.start()
    m2 = mp.Process(target=is_show,args=(isshow,))
    m2.start()
    #执行是相当与开启了3个进程
