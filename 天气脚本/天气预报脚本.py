import requests
import json
import logging as log
# 1、导入模块
import yagmail
# 2、设置smtp服务信息
yag = yagmail.SMTP(user="2247124474@qq.com",
                   password="xoqivkzaipbqecdh", host='smtp.qq.com')


def get_weather_wind(url):
    r = requests.get(url)
    if r.status_code != 200:
        log.error("Can't get weather data!")
    info = json.loads(r.content.decode())

    # get wind data
    data = info['data']
    WD = data['list'][0]
    wind = WD['wind']
    airQuality = WD['airQuality']
    return "{}({})".format(wind, airQuality)


def get_weather_city(url, city):
    # open url and get return data
    r = requests.get(url)
    if r.status_code != 200:
        log.error("Can't get weather data!")

    # convert string to json
    info = json.loads(r.content.decode())

    # get useful data
    # data = info['weatherinfo']
    # city = data['city']  # 城市
    # temp1 = data['temp1']  # 最低温度
    # temp2 = data['temp2']  # 最高温度
    # weather = data['weather']  # 天气

    # get wind data
    data = info['data']
    WD = data['list'][0]
    weather = WD['weather']
    low = WD['low']
    high = WD['high']
    return "{}  {}  {}°~{}° ".format(city, weather, low, high)

# 101200101 武汉

# 10101: "北京"
# 10102: "上海"
# 10103: "天津"
# 10104: "重庆"
# 10105: "黑龙江"
# 10106: "吉林"
# 10107: "辽宁"
# 10108: "内蒙古"
# 10109: "河北"
# 10110: "山西"
# 10111: "陕西"
# 10112: "山东"
# 10113: "新疆"
# 10114: "西藏"
# 10115: "青海"
# 10116: "甘肃"
# 10117: "宁夏"
# 10118: "河南"
# 10119: "江苏"
# 10120: "湖北"
# 10121: "浙江"
# 10122: "安徽"
# 10123: "福建"
# 10124: "江西"
# 10125: "湖南"
# 10126: "贵州"
# 10127: "四川"
# 10128: "广东"
# 10129: "云南"
# 10130: "广西"
# 10131: "海南"
# 10132: "香港"
# 10133: "澳门"
# 10134: "台湾"


if __name__ == '__main__':
    msg = """天气提醒🔊:   
{} {}
来源: 墨迹天气
""".format(
        get_weather_city(
            'https://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=杭州&latitude=39.902895&longitude=116.427915&needMoreData=true&pageNo=1&pageSize=7','杭州'),
        get_weather_wind('https://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=杭州&latitude=39.902895&longitude=116.427915&needMoreData=true&pageNo=1&pageSize=7'),
        # get_weather_city('http://www.weather.com.cn/data/cityinfo/101210101.html'),
        # get_weather_wind('http://www.weather.com.cn/data/sk/101210101.html')
    )

# 3、设置邮件主题与邮件内容
subject = '天气预报⛅'
content = [msg]
# 4、发送邮件
yag.send('2273425653@qq.com', subject, content)

print(msg)
