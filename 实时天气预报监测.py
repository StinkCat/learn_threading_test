# -*- coding: UTF-8 -*-
#利用抓取到的MIUI天气分钟级接口实时监测未来两小时天气预警
#实现功能：提示天气情况，未来两小时将要下雨的话电脑会发出“哔哔哔”告警
import multiprocessing as mp
import  threading
import winsound
import datetime
import requests
import  time

lon = 126.4244300000
lat = 41.9408000000
def Myprint(): #次线程打印输出
    global Tips
    while True:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(nowTime+" : "+Tips)
            time.sleep(3)

def Warning(iswarn): #次进程发出告警
    while True:
        while iswarn.value ==1:
            winsound.Beep(520, 1000)
            time.sleep(1)
def getlocation(): #获取经纬度的地理位置
    pass
def getWeather():
    url = 'https://weatherapi.market.xiaomi.com/wtr-v3/weather/xm/forecast/minutely?latitude='+str(lat)+'&longitude='+str(lon)+'&locale=zh_cn&isGlobal=false&appKey=weather20151010&locationKey=weathercn%2b101010101&sign=jieyongAPI0buhuilanyong'
    headers = {
        'Accept-Encoding': 'gzip',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; MI 6 MIUI/V10.0.2.0.OCACNFH)',
        'Connection': 'keep-alive',
        'Host': 'weatherapi.market.xiaomi.com',
    }
    resp = requests.get(url, headers=headers)
    result = resp.json()['precipitation']
    headDescription = result["headDescription"] #判定降雨量结果
    Tips = result["description"] #综合提示结果
    rainfall = result["value"] #未来降雨量
    return [headDescription,Tips,rainfall]
    pass
if __name__ == '__main__':
    Sleeptime = 15
    Tips = "正在监测未来两小时天气预警"
    My_print = threading.Thread(target=Myprint)
    My_print.start()
    iswarn = mp.Value("i", 0)  # 初始赋值为0
    warn = mp.Process(target=Warning, args=(iswarn,))
    warn.start()
    while True:
        results = getWeather()
        Tips = results[1]
        Min = 0
        for temp in results[2]:
            Min += 1
            if temp > 0:
                iswarn.value = 1
                Tips = "{0},{1}分钟后降雨量为{2}".format(results[1],Min,temp)
                Sleeptime = 5
                break
        time.sleep(Sleeptime)
