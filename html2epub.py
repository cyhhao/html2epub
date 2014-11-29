# coding:utf8
import os
import shutil
import htmlcl
import zipFile


class html2epub:
    def __init__(self, Path, Topath):
        # 得到两个路径
        self.path = self.Path2Std(Path)
        self.toPath = self.Path2Std(Topath)

    def start(self):
        # 举出html存放路径下所有文件
        all_file = os.listdir(self.path)

        # print all_file
        for each in all_file:
            print each
            if not each.endswith('.html'):
                continue
            # 新建一个temp文件夹用来组织zip包里的内容
            # 如果已经存在则删除temp文件夹
            if os.path.exists('temp'):
                shutil.rmtree('temp')
            # 复制粘贴
            shutil.copytree('resource', 'temp')
            # 创建存放图片的目录
            os.makedirs('temp/oebps/image')

            # 组合文件名
            name = each.decode('utf-8')
            FilePath = self.path + name

            #第一步：修改content.opf文件的title
            file0 = open(r'resource/content.opf', 'r')
            change = file0.read()
            file0.close()

            OnlyName = name.replace('.html', '')
            change = change.replace('<dc:title>', '<dc:title>' + OnlyName)   # 很粗暴的替换
            change = change.replace('content="', 'content="' + OnlyName)     # 很粗暴的替换
            file0 = open(r'temp/content.opf', 'w')
            file0.write(change)
            file0.close()
            # 第一个要处理的文件处理完了

            # 第二步：处理HTML文件
            file1 = open(FilePath, 'r')
            index = file1.read()
            file1.close()

            # 写一个解析类，负责下载html中的图片，并放入特定的路径下，并修改HTML文件中的图片路径
            rep = [index]
            Parser = htmlcl.get_img(html=rep, path=r'temp/')
            # print index
            Parser.feed(index)
            # print rep[0]

            #把改好的html写入文件
            file1 = open(r'temp/index.html', 'w')
            file1.write(rep[0])
            file1.close()

            # 第三步：zip压缩修改好的文件，命名为.epub后缀
            zipFile.zip_dir(r'temp', self.toPath + OnlyName + '.epub')

            # 删除临时的文件夹
            shutil.rmtree('temp')
            print '所有已完成'




    def Path2Std(self, Path):

        Path = Path.decode('utf-8')
        Path = Path.replace('\\', '/')

        if Path.endswith('/'):
            pass
        else:
            Path += '/'

        # print Path
        return Path