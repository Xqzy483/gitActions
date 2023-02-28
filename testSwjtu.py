import requests
from bs4 import BeautifulSoup
import json


def get_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Cookie': "username=2019113645; JSESSIONID=9C5FC8B593ABCE6C550F78DF41C8D926; Hm_lvt_87cf2c3472ff749fe7d2282b7106e8f1=1677464566,1677505442,1677557711,1677575057; Hm_lpvt_87cf2c3472ff749fe7d2282b7106e8f1=1677580450",
    }
    url = "http://jwc.swjtu.edu.cn/vatuu/StudentScoreInfoAction?setAction=studentScoreQuery&viewType=studentScore&orderType=submitDate&orderValue=desc"
    # http: // jwc.swjtu.edu.cn / vatuu / StudentScoreInfoAction?setAction = studentScoreQuery & viewType = studentScore & orderType = submitDate & orderValue = desc
    # parmes = {'headers': headers}
    r = requests.get(url, headers=headers)
    html = r.content.decode('utf-8', 'ignore')
    soup = BeautifulSoup(html, 'html.parser')
    return soup


if __name__ == '__main__':
    re = get_data()
    print(re)
