import re

'''
贪婪匹配与非贪婪匹配
贪婪匹配是尽可能匹配多的字符，非贪婪匹配就是尽可能匹配少的字符。
'''
print('--------贪婪匹配---------------')
content = 'bluehonour has 100 banaanas'
# 贪婪匹配(默认)
res = re.match('^(.*)(\d+)(.*)$', content)
print(res.string)  # bluehonour has 100 banaanas
print('group(1):', res.group(1), '; group(2):', res.group(2), '; group(3):', res.group(3))
# group(1): bluehonour has 10 ; group(2): 0 ; group(3):  banaanas
# 在贪婪匹配下，.* 会匹配尽可能多的字符。正则表达式中.*后面是\d+，也就是至少一个数字，并没有指定具体多少个数字，
# 因此，.*就尽可能匹配多的字符，这里就把10匹配了，给\d+留下个可满 足条件的数字 0.最后得到的内容就只有数字0了。

print('--------非贪婪匹配---------------')
# 非贪婪匹配
# 但这很明显会给我们带来很大的不便。有时候，匹配结果会莫名其妙少了部分内容。
# 其实，这里只需要使用非贪婪匹配就好了。非贪婪匹配的写法是.*?，多了一个?，那么它可以达到怎样的效果?我们再用实例看一下:
res = re.match('(.*?)(\d+)(.*)$', content)
print('group(1):', res.group(1), '; group(2):', res.group(2), '; group(3):', res.group(3))
# group(1): bluehonour has  ; group(2): 100 ; group(3):  banaanas

'''
但是 .* 中的.只能匹配除了 \n \r的单个字符，那么遇到换行怎么办呢?
答案是使用 re.S
'''
print('--------re.S---------------')
content = """bluehonour has 100 
banaanas"""
res = re.match('^(.*)(\d+)(.*)$', content, re.S)
print('group(1):', res.group(1), '; group(2):', res.group(2), '; group(3):', res.group(3))

print('--------re.search---------------')
'''
re.search: 直接扫描字符串，不需要匹配字符串的开头和结尾，会把匹配成功的第一个字符串返回给你
'''
content = """bluehonour has 100 
banaanas"""
res = re.search('(.*)(\d+)(.*)', content, re.S)
print('group(1):', res.group(1), '; group(2):', res.group(2), '; group(3):', res.group(3))

'''
re.findall: 获取所有匹配的内容
'''
print('--------re.findall---------------')
content = """bluehonour has 100 banaanas
bluehonour has 300 banaanas
bluehonour has 200 banaanas"""
res = re.findall('.*?(\d+).*?', content, re.S)
print(res) # ['100', '300', '200']

'''
re.sub: 调换匹配的内容
'''
print('--------re.sub---------------')
content = 'bluehonour has 100 banaanas'
content = re.sub('(\d+)','888', content)
print(content) # bluehonour has 888 banaanas

'''
re.compile： 便于以后复用
'''
print('--------re.compile---------------')
content = 'bluehonour has 100 banaanas'
pattern = re.compile('.*?(\d+).*?', re.S)
res = re.match(pattern, content)
# 等同于 res = re.match('.*?(\d+).*?', content, re.S)
print(res.groups(1)) # ('100',)

