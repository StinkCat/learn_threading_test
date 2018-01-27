# -*- coding: UTF-8 -*-
import  re
import  time
import requests
import  threading

counter = 0
lock = threading.RLock()
def load():
    try:
        f = open("./mingdan.txt","r")
        s = f.read()
        f.close()
        pattern = re.compile('.*?(《.*?》).*?',re.S)#使用正则表达式创建对象
        itemts = re.findall(pattern,s)#匹配对象
        print(len(itemts))
        # for item in itemts:
        #     print(item)
        return itemts
    except:
        print("读取文件出错")
    finally:
         pass

def search(N):
    global counter
    # lock.acquire()  # 枷锁(加锁后的代码部分线程轮流提取值，相当于轮流执行一个线程，变量不会打乱)
    start_time = time.time()
    url = "http://m.baidu.com"
    try:
        r = requests.get(url,data = {"word":N},timeout = 10)
    except requests.exceptions.ConnectionError:
        counter =counter+1
        print("%countre访问超时:%s"%(counter,N))
        # lock.release()  # 解锁
    else:
        if r.status_code == 200:
            # time.sleep(10)
            end_time = time.time()
            counter = counter + 1
            Time = (end_time - start_time) * 1000
            print(counter,"访问成功:%s，耗时%.2fms"%(N,Time), '当前线程的名字是： ', threading.current_thread().name)
            # print(r.text)
        elif r.status_code == 403:
            print("可能IP被封杀啦...%s"%threading.current_thread().name)
        # lock.release()  # 解锁
    # time.sleep(10)
# def get_mingzi():
#     itemts = load()
#     for n in itemts:
#         yield  n

def main():
    itemts = load()
    t1 = time.time()
    thread_list = []
    number = 0
    i = 0
    print('这是主线程：', threading.current_thread().name)
    for n in itemts:
        number = number+1
        # s = get_mingzi()
        t = threading.Thread(target=search, args=(n[1:-1],),name= "大傻"+str(number))
                        #target: 要执行的方法；args/kwargs: 要传入方法的参数；name: 线程名
        thread_list.append(t)#添加进线程列表

    for t in thread_list:
        t.setDaemon(False)
        #is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）
# 　　　 如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
#        如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
        time.sleep(0.03)#加入停止时间可以避免线程过多拥塞或者网速拥塞出错
        # time.sleep(2)
        t.start()
    t.join()#阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
    print("返回主线程，子线程数%s"%number)
    hs = (time.time()-t1)
    print("总耗时%.2f秒"%hs)


if __name__ == '__main__':
    main()
