import requests as req
from bs4 import BeautifulSoup
import time, datetime


def data():
    urls_list = []
    html = req.get('http://www.lingjuw.cn')
    soup = BeautifulSoup(html.text, "html.parser").select('.content-wrap .content .excerpt a')
    for url in soup:
        if url['href'] != 'javascript:;':
            urls_list.append(url['href'])
    return urls_list


def main(urls):
    param = {
		"site": "www.lingjuw.cn",
        "token": "你的百度token值"
    }
    header = {
        "User-Agent": "curl/7.12.1",
        "Content-Type": "text/plain",
    }
    url = "http://data.zz.baidu.com/urls"
    send_data = '\n'.join(set(urls))
    try:
	    data = req.post(url, params=param, headers=header, data=send_data, timeout=10)
    except Exception as e:
    	print(e)
    else:
	    success = data.json().get('success')
	    remain = data.json().get('remain')
    if success:
        print(f"提交成功,这次提交了{success}条,还有{remain}次提交次数")


if __name__ == '__main__':
    while True:
        urls = data()
        urls.append('http://www.lingjuw.cn/sitemap.xml')
        main(urls)
        # print(datetime.datetime.now().hour)
        time.sleep(10)
