# 以前的low到爆炸的代码...
import requests as req
from bs4 import BeautifulSoup

def GetUrl():
    """获取下载链接和文件名"""
    # 班课下载资源地址
    url = "https://www.mosoteach.cn/web/index.php?c=res&m=index&clazz_course_id=509ABFF6-CB61-11E8-AA22-7CD30AD36C02"
    htmls = req.get(url,headers=header)
    soup = BeautifulSoup(htmls.text,"html.parser")
    # 获取文件名字
    title = soup.select(".hide-div .res-name")
    # 获取下载链接
    DownUrl = soup.select(".hide-div .res-row-open-enable")
    return title,DownUrl

def DownFile(url,title):
    """获取到的链接进行下载"""
    data = req.get(url,headers=header)
    with open(title,"wb") as f:
        f.write(data.content)
        f.close()
    print("%s下载完成"%title)


# 蓝墨云登录的cookie
cookie = "你登录的cookie"
header = {
    "Cookie": cookie,
    "User-Agent": "Mozilla/5.0"
}

def main():
    title,DownUrl = GetUrl()
    i = 0
    for d in DownUrl:
        url = d['data-href']
        titles = title[i].text
        # 判断如果文件是MP4 或者是zip就不下载了
        if titles.split(".")[-1] == "mp4" or titles.split(".")[-1] == "zip":
            pass
        else:
            DownFile(url, titles)
        i+=1

if __name__ == '__main__':
    main()
