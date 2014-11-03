import HTMLParser
import hashlib
import urllib


class get_img(HTMLParser.HTMLParser):
    def __init__(self, html, path):
        self.html = html
        self.path = path
        HTMLParser.HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for key, value in attrs:
                if key == "src":
                    hash = hashlib.md5(value).hexdigest().upper()[0:8]
                    new_url = "oebps/image/" + hash + '.png'
                    urllib.urlretrieve(value, self.path + new_url)

                    print key, value, hash

                    self.html[0] = self.html[0].replace(value, new_url)



