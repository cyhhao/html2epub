# coding:utf8
import HTMLParser
import hashlib
import urllib

# 继承于Python自带的HTMLParser解析类
import urllib2


class get_img(HTMLParser.HTMLParser):
    def __init__(self, html, path):
        self.html = html
        self.path = path
        HTMLParser.HTMLParser.__init__(self)

    # 当标签开始的时候
    def handle_starttag(self, tag, attrs):
        # 如果标签是img标签
        if tag == 'img':
            for key, value in attrs:
                # 取<img>标签的src属性
                if key == "src":
                    # 哈希url，得到一会儿要保存的唯一的图片名
                    hash = hashlib.md5(value).hexdigest().upper()[0:8]
                    new_url = "oebps/image/" + hash + '.png'

                    # 下载图片并保存
                    # print value
                    # opener=urllib2.build_opener()
                    # req=urllib2.Request(value)
                    # req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36")
                    # req.add_header("If-None-Match",'"1153673238\"')
                    # res=opener.open(req)
                    # f = open(self.path + new_url,'wb')
                    # f.write(res.read())
                    try:
                        i_headers = {
                            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",
                            "Accept": "text/plain"}

                        req = urllib2.Request(value, headers=i_headers)
                        res = urllib2.urlopen(req)
                        f = open(self.path + new_url, "wb")
                        f.write(res.read())

                        # urllib.urlretrieve(value, self.path + new_url)
                    except Exception:
                        print Exception
                    print key, value, hash

                    # 替换HTML中的图片路径为本地图片路径
                    self.html[0] = self.html[0].replace(value, new_url)
