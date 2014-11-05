# coding:utf8
import sys
from html2epub import html2epub

reload(sys)
sys.setdefaultencoding('utf8')

sys.getdefaultencoding()

if __name__ == '__main__':
    path = raw_input('请输入需要转换的HTML存放目录：')
    ToPath = raw_input('请输入生成的epub存放目录：')

    zh = html2epub(path, ToPath)
    zh.start()



