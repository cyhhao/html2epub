import os
import shutil
import htmlcl
import zipFile


class html2epub:
    def __init__(self, Path, Topath):

        self.path = self.Path2Std(Path)
        self.toPath = self.Path2Std(Topath)

    def start(self):
        all_file = os.listdir(self.path)

        print all_file
        for each in all_file:
            print each
            shutil.copytree('resource', 'temp')

            name = each.decode('utf-8')

            FilePath = self.path + name
            file0 = open(r'resource/content.opf', 'r')
            change = file0.read()
            file0.close()

            OnlyName = name.replace('.html', '')
            change = change.replace('<dc:title>', '<dc:title>' + OnlyName)
            change = change.replace('content="', 'content="' + OnlyName)
            file0 = open(r'temp/content.opf', 'w')
            file0.write(change)
            file0.close()

            file1 = open(FilePath, 'r')
            index = file1.read()
            file1.close()

            rep = [index]
            Parser = htmlcl.get_img(html=rep, path=r'temp/')
            Parser.feed(index)
            # print rep[0]

            file1 = open(r'temp/index.html', 'w')
            file1.write(rep[0])
            file1.close()

            zipFile.zip_dir(r'temp', self.toPath + OnlyName + '.epub')

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