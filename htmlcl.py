# coding:utf8
import HTMLParser
import hashlib
import urllib

# 继承于Python自带的HTMLParser解析类
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
                    urllib.urlretrieve(value, self.path + new_url)

                    print key, value, hash

                    # 替换HTML中的图片路径为本地图片路径
                    self.html[0] = self.html[0].replace(value, new_url)



