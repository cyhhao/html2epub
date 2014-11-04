# 一个简单的HTML转epub格式的Python程序

## 文件说明：

### 1. html2epub.py   
	# 可直接实例化调用
	# 传入path要转换的文件所在路径以及生成文件的路径
	zh = html2epub(path, ToPath)
    zh.start()

### 2. main.py
一个示例，可直接从main运行此转换工具。

### 3. htmlcl.py
html解析并下载图片等操作的类，html2epub类依赖此类。

### 4. zipFile.py
压缩操作，html2epub类依赖此类。

### 5. resource
内含生成epub所必须的资源文件。

### 注意：此程序运行需联网

## 希望能帮更多的人

之前写过一个爬廖雪峰的Python教程的程序，无奈爬下来的是html。想在kindle上看，找到了这个[在线转epub的网站](http://html.toepub.com/)。

但是这个网站转出来的epub没有图片，所以一直在找更靠谱的转换工具。发现epub本质上就是一堆xml配置文件+html+css打了一个zip包，所以就试着做了一下。

希望能帮助和我一样，在寻求可以把html带到kindle上看的人们。