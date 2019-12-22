#### 1.什么是BeautifulSoup
Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.

#### 2.安装 Beautiful Soup
1. 如果你用的是新版的Debain或ubuntu,那么可以通过系统的软件包管理来安装:
	
	`$ apt-get install Python-bs4`
2. Beautiful Soup 4 通过PyPi发布,所以如果你无法使用系统包管理安装,那么也可以通过 easy_install 或 pip 来安装.包的名字是 beautifulsoup4 ,这个包兼容Python2和Python3.

    `$ easy_install beautifulsoup4`

    `$ pip install beautifulsoup4`
3. (在PyPi中还有一个名字是 BeautifulSoup 的包,但那可能不是你想要的,那是 [Beautiful Soup3](https://www.crummy.com/software/BeautifulSoup/bs3/documentation.html) 的发布版本,因为很多项目还在使用BS3, 所以 BeautifulSoup 包依然有效.但是如果你在编写新项目,那么你应该安装的 beautifulsoup4 )

4. 如果你没有安装 easy_install 或 pip ,那你也可以 下载[BS4](https://www.crummy.com/software/BeautifulSoup/bs4/download/4.0/)的源码 ,然后通过setup.py来安装.
	
	`$ Python setup.py install`
5. 如果上述安装方法都行不通,Beautiful Soup的发布协议允许你将BS4的代码打包在你的项目中,这样无须安装即可使用.

#### 3.安装解析器
1. Beautiful Soup支持Python标准库中的HTML解析器,还支持一些第三方的解析器,其中一个是 [lxml](https://lxml.de/) .根据操作系统不同,可以选择下列方法来安装lxml:

	`$ apt-get install Python-lxml`

	`$ easy_install lxml`

	`$ pip install lxml`

2. 另一个可供选择的解析器是纯Python实现的 [html5lib](https://github.com/html5lib/) , html5lib的解析方式与浏览器相同,可以选择下列方法来安装html5lib:

	`$ apt-get install Python-html5lib`

	`$ easy_install html5lib`

	`$ pip install html5lib`


#### 4.下表列出了主要的解析器,以及它们的优缺点:

![解析器比较](https://i.imgur.com/xWCjPGq.png)

推荐使用lxml作为解析器,因为效率更高. 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib, 因为那些Python版本的标准库中内置的HTML解析方法不够稳定.

提示: 如果一段HTML或XML文档格式不正确的话,那么在不同的解析器中返回的结果可能是不一样的,查看 [解析器之间的区别](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#id53) 了解更多细节


#### 5.如何使用
    from bs4 import BeautifulSoup
	
	html_doc = """
	<html><head><title>The Dormouse's story</title></head>
	<body>
	<p class="title"><b>The Dormouse's story</b></p>
	
	<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
	and they lived at the bottom of a well.</p>
	
	<p class="story">...</p>
	"""

	#格式化输出
	print(soup.prettify())
	soup.title
	# <title>The Dormouse's story</title>
	
	soup.title.name
	# u'title'
	
	soup.title.string
	# u'The Dormouse's story'
	
	soup.title.parent.name
	# u'head'
	
	soup.p
	# <p class="title"><b>The Dormouse's story</b></p>
	
	soup.p['class']
	# u'title'
	
	soup.a
	# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
	
	soup.find_all('a')
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
	
	soup.find(id="link3")
	# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


#### 6.中文参考文档

[https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/# "中文参考文档")