#### 什么是selenium

selenium 是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。
Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。
selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。

#### selenium的安装
    pip install selenium

#### 下载浏览器驱动
|浏览器|下载地址（选择对用的驱动程序下载）|
|:-:|:-|
|Chrome|	https://sites.google.com/a/chromium.org/chromedriver/downloads|
|Edge|https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/|
|Firefox|	https://github.com/mozilla/geckodriver/releases|
|Safari|https://webkit.org/blog/6900/webdriver-support-in-safari-10/|

下载完之后解压到某个文件夹下，并配置环境变量

#### 常用的查找元素方法

    from selenium import webdriver

	driver = webdriver.Firefox() #创建了一个 Firefox 驱动
	driver.get("https://www.baidu.com") #使用 get 方法打开百度
	input = driver.find_element_by_css_selector('#kw')

1. find_element_by_name
2. find_element_by_id
3. find_element_by_xpath
4. find_element_by_link_text
5. find_element_by_partial_link_text
6. find_element_by_tag_name
7. find_element_by_class_name
8. find_element_by_css_selector

#### find_elements方法查找元素
下面这种方式是比较通用的一种方式：这里需要记住By模块所以需要导入

    from selenium import webdriver
	from selenium.webdriver.common.by import By

	browser = webdriver.Chrome()
	browser.get("https://www.taobao.com")
	browser.find_elements(By.CSS_SELECTOR,'.service-bd li').find_elements(By.ID, 'xxx')

1. ID = "id"
2. XPATH = "xpath"
3. LINK_TEXT = "link text"
4. PARTIAL_LINK_TEXT = "partial link text"
5. NAME = "name"
6. TAG_NAME = "tag name"
7. CLASS_NAME = "class name"
8. CSS_SELECTOR = "css selector"


#### 多个元素查找
其实多个元素和单个元素的区别，举个例子：find_elements,单个元素是find_element,其他使用上没什么区别

    browser.find_elements(By.CSS_SELECTOR,'.service-bd li')

1. find_elements_by_name
2. find_elements_by_id
3. find_elements_by_xpath
4. find_elements_by_link_text
5. find_elements_by_partial_link_text
6. find_elements_by_tag_name
7. find_elements_by_class_name
8. find_elements_by_css_selector

#### 交互动作
    from selenium import webdriver
	from selenium.webdriver import ActionChains
	
	browser = webdriver.Chrome()
	
	url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
	browser.get(url)
	browser.switch_to.frame('iframeResult')
	source = browser.find_element_by_css_selector('#draggable')
	target = browser.find_element_by_css_selector('#droppable')
	actions = ActionChains(browser)
	actions.drag_and_drop(source, target)
	actions.perform()

#### 执行JavaScript
    from selenium import webdriver
	browser = webdriver.Chrome()
	browser.get("http://www.zhihu.com/explore")
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
	browser.execute_script('alert("To Bottom")')

----------

    JS控制滚动条的位置：
	window.scrollTo(x, y);
	
	竖向滚动条置顶 window.scrollTo(0, 0);
	竖向滚动条置底window.scrollTo(0, document.body.scrollHeight)
	
	JS控制TextArea滚动条自动滚动到最下部
	document.getElementById('textarea').scrollTop = document.getElementById('textarea').scrollHeight



#### 官方文档
[https://selenium-python.readthedocs.io/](https://selenium-python.readthedocs.io/ "官方文档")

#### 中文参考文档
[https://selenium-python-zh.readthedocs.io/en/latest/](https://selenium-python-zh.readthedocs.io/en/latest/)
[https://python-selenium-zh.readthedocs.io/zh_CN/latest/](https://python-selenium-zh.readthedocs.io/zh_CN/latest/ "中文参考文档")
