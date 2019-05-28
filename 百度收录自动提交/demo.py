import requests as req
from bs4 import BeautifulSoup
import time, datetime, os


def data():
    urls_list = []
    head = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36",
        "Cookie": "wordpress_logged_in_1cee09977a7e7e6f5284dd84fabf6113=fengxi%7C1559257983%7CgAvt1vw1b4nWV9Nop1kaKuvS3E0pnwLAkfOEQ75LA4B%7C33d8d13e8bdef9317f89d413835461171b133c0de9910c724466537d6da01af0; wp-settings-1=libraryContent%3Dbrowse; wp-settings-time-1=1558048383; UM_distinctid=16ac2ecdb072bd-0ef06f08f09da5-e323069-19fa51-16ac2ecdb08237; CNZZDATA1262045946=794321775-1558044950-%7C1558246334"
    }
    filename = './data'
    try:
        if not os.path.exists(filename):
            html = req.get('http://www.lingjuw.cn/sitemap.xml', timeout=5, headers=head)
            with open(filename, 'wb') as f:
                f.write(html.content)
            soup = BeautifulSoup(html.text, "lxml").select('loc')
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                html = f.read()
            # print(html)
            soup = BeautifulSoup(html, "lxml").select('loc')
        time.sleep(0.01)

    except Exception as e:
        print(e)
    else:
        for url in soup:
            urls_list.append(url.text)
    return urls_list


def main(urls):
    param = {
        "site": "www.lingjuw.cn",
        "token": "你的token值"
    }
    header = {
        "User-Agent": "curl/7.12.1",
        "Content-Type": "text/plain",
    }
    url = "http://data.zz.baidu.com/urls"
    send_data = '\n'.join(set(urls))
    try:
        data = req.post(url, params=param, headers=header, data=send_data, timeout=10)
        success = data.json().get('success')
        remain = data.json().get('remain')
        if success:
            print(success, remain)
    except Exception as e:
        print(e)
    else:
        print("OK!")


if __name__ == '__main__':
    while True:
        urls = data()
        urls.append('http://www.lingjuw.cn/sitemap.xml')
        main(urls)
        time.sleep(0.2)
