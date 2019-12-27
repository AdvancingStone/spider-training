

#### 1.什么是 phantomJS
它是一个基于 WebKit 的浏览器引擎，可以做到无声无息的操作各种动态网站。比如 js，css选择器，dom操作的，所以对于市面上大多通过 js 渲染的动态网站，难以解析的网站，想要爬取的话就会使用到selenium + phantomjs

#### 2.下载 phantomJS
https://github.com/fandsimple/chrome_copy

下载完之后要配置环境变量，将bin目录配置到path路径下

#### 3.最新版本的selenium已不支持phantomJS
* 卸载selenium

    `pip uninstall selenium`
    
* 安装旧版本的，推荐2.53.6，使用参数--default-timeout=100，否则报超时

    `pip --default-timeout=100 install selenium==2.53.6`

#### 4.代替phantomJS
不弹出界面，实现无界面爬取
    
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.firefox.options import Options

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Firefox(options=options)

#### 5.问题
    selenium.common.exceptions.SessionNotCreatedException: Message: session not created: No matching capabilities found

因为chrome或Firefox的驱动版本对应浏览器版本不一致，下面提供两个地址：
http://chromedriver.storage.googleapis.com/index.html
http://npm.taobao.org/mirrors/chromedriver/

但是谷歌浏览器版本为 79.0.3945.88 的是个大坑，找不到对应的驱动程序