from selenium import webdriver

# 打开Chrome浏览器，并用百度搜索苍老师照片

# driver = webdriver.Chrome() #创建了一个 Chrome 驱动
driver = webdriver.Firefox() #创建了一个 Firefox 驱动
driver.get("https://www.baidu.com") #使用 get 方法打开百度
input = driver.find_element_by_css_selector('#kw')
input.send_keys("苍老师照片")
button = driver.find_element_by_css_selector('#su')
button.click()

# 获取请求链接
# print(driver.current_url)
# 获取 cookies
# driver.get_cookie() #此处行不通
# 获取源代码
# print(driver.page_source)
# 获取搜索框url的值
# print(input.text)

