from bs4 import BeautifulSoup

html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc,'lxml')
# 获取标题的内容
print(soup.title.string)    #学习python的正确姿势
# 获取 p 标签里面的内容
print(soup.p.string)    #小帅b的故事
# 获取 title 的父级标签
print(soup.title.parent.name)   #head
# 获取超链接
print(soup.a)   #<a class="sister" href="http://example.com/1" id="link1">一个笑话长</a>
# 获取所有超链接
print(soup.find_all('a'))#[<a class="sister" href="http://example.com/1" id="link1">一个笑话长</a>, <a class="sister" href="http://example.com/2" id="link2">一个笑话短</a>]
# 获取 id 为 link2 的超链接
print(soup.find(id="link2"))#<a class="sister" href="http://example.com/2" id="link2">一个笑话短</a>
# 获取网页中所有的内容
print(soup.get_text())
'''
# 学习python的正确姿势

小帅b的故事
有一天，小帅b想给大家讲两个笑话
一个笑话长,
一个笑话短 ,
他问大家，想听长的还是短的？
...
'''

# css选择器，id前加#， class前加.
print(soup.select("title")) #[<title>学习python的正确姿势</title>]
# 返回body下的所有a标签，逐层查找
print(soup.select("body a")) #[<a class="sister" href="http://example.com/1" id="link1">一个笑话长</a>, <a class="sister" href="http://example.com/2" id="link2">一个笑话短</a>]
# 返回p标签下的id为link1的直接子标签
print(soup.select("p > #link1")) #[<a class="sister" href="http://example.com/1" id="link1">一个笑话长</a>]

# 想进一步学习，参考以下网址
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/