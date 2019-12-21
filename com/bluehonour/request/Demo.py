import requests

# get请求
# r = requests.get('https://www.baidu.com')
# print(r.text)

# post请求
# r = requests.post('https://httpbin.org/post', data = {'key':'value'})
# print(r.text)

# 其他请求
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')

# 请求携带参数
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', params=payload)

# headers假装自己是个浏览器
# stream流
url = 'https://api.github.com/events'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers, stream=True)
# 获取服务器响应文本内容
print(r.text)
# 获取服务器响应编码
print(r.encoding)
# 获取字节响应内容
print(r.content)
# 获取响应码
print(r.status_code)
# 获取响应头
print(r.headers)
# 获取json响应内容
print(r.json())
# 获取socket流响应内容
print(r.raw)
print(r.raw.read(4))

# post请求
# 当你想要在一个键里面添加多个值的时候
url = 'https://httpbin.org/post'
payload_tuples = [('key', 'value1'), ('key', 'value2')]
r1 = requests.post(url, data=payload_tuples)
print(r1.content)
payload_dict = {'key':['value1', 'value2']}
r2 = requests.post(url, data=payload_dict)
print(r2.content)
print(r1.text==r2.text)  # True

# 请求的时候用json作为参数
url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
r = requests.post(url, json=payload)
print(r.text)

# 上传文件
url = 'https://httpbin.org/post'
files = {'file': open('report.txt', 'rb')}
r = requests.post(url, files=files)
print(r.text)


# 获取cookie信息
url = 'http://example.com/some/cookie/setting/url'
r = requests.get(url)
print(r.cookies)
print(r.cookies['example_cookie_name'])

# 发送cookie信息
url = 'https://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

# 设置超时
r = requests.get('https://github.com/', timeout=0.001)
print(r.text)