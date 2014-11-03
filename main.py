# coding:utf8
import os
import shutil


shutil.copytree('resource', 'temp')

path = raw_input('请输入需要转换的HTML存放目录：')
path = path.decode('utf-8')
path = path.replace('\\', '/')

if path.endswith('/'):
    pass
else:
    path += '/'

print path

all_file = os.listdir(path)

print all_file
for each in all_file:
    FilePath = path + each
    file0 = open(r'resource/content.opf', 'r')
    change = file0.read()
    file0.close()

    change = change.replace('<dc:title>', '<dc:title>' + each)
    change = change.replace('content="', 'content="' + each)
    file0 = open(r'resource/content.opf', 'w')
    file0.write(change)
    file0.close()

    file1 = open()


#
# file0 = open(r'resource/content.opf', 'r')
#
# print file0.read()
#
# change = file0.read()
# change.
#
# change.close()
#
# shutil.rmtree('temp')



