from urllib import request,parse
import ssl

# urlopen 默认为get请求，当传入参数时为post请求
# request 的 urlopen 方法可以传入的参数主要有 3 个
# urllib.request.urlopen(url, data=None, [timeout, ]*)
# url: 表示请求的链接
# data: 供post请求携带参数用的，data可以用 byte类型传递
# timeout：设置请求超时时间
# response = request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# Request 可以让我们自己定义请求的方式
# 这样我们就可以使用 Request 来封装我们的请求信息
# 增加请求头信息，使用 request中的Request方法
# urllib.request.Request(url, data=None, headers={}, method=None)

url = 'https://www.taobihu.com/account/ajax/login_process/'
headers = {
    #假装自己是浏览器
    'User-Agent':' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
# 逼乎这个b用的是 https, 使用 ssl 未经验证的上下文
context = ssl._create_unverified_context()
# 定义一下我们的请求参数
dict = {
    'return_url':'https://www.taobihu.com/',
    'user_name':'xxxxxxxxxx@qq.com',
    'password':'xxxxxxxxxxx',
    # 'net_auto_login':'1',
    '_post_type':'ajax',
}
# 把请求的参数转化为 byte
data = bytes(parse.urlencode(dict),'utf-8')
# 封装request请求
req = request.Request(url, data=data, headers=headers, method='post')
response = request.urlopen(req, context=context)
print(response.read().decode('utf-8'))