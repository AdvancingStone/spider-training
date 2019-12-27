#### [开源 ip 代理池](https://github.com/Python3WebSpider/ProxyPool.git)
[https://github.com/Python3WebSpider/ProxyPool.git](https://github.com/Python3WebSpider/ProxyPool.git)

#### 使用方式

### 1. 首先使用 git clone 将源代码拉到你本地

		git clone https://github.com/Python3WebSpider/ProxyPool.git

### 2. 接着打开项目中的 setting.py,在这里可以配置相关信息,比如 Redis 的地址密码相关
（如果你之前没有使用过 redis 的话，可以到如下[地址下载](https://github.com/MicrosoftArchive/redis/releases)）

		# Redis数据库地址
		REDIS_HOST = '127.0.0.1'
		
		# Redis端口
		REDIS_PORT = 6379
		
		# Redis密码，如无填None
		REDIS_PASSWORD = None
		
		REDIS_KEY = 'proxies'
		
		# 代理分数
		MAX_SCORE = 100
		MIN_SCORE = 0
		INITIAL_SCORE = 10
		
		VALID_STATUS_CODES = [200, 302]
		
		# 代理池数量界限
		POOL_UPPER_THRESHOLD = 50000
		
		# 检查周期
		TESTER_CYCLE = 20
		# 获取周期
		GETTER_CYCLE = 300
		
		# 测试API，建议抓哪个网站测哪个
		TEST_URL = 'http://www.baidu.com'
		
		# API配置
		API_HOST = '0.0.0.0'
		API_PORT = 5555
		
		# 开关
		TESTER_ENABLED = True
		GETTER_ENABLED = True
		API_ENABLED = True
		
		# 最大批测试量
		BATCH_TEST_SIZE = 10



### 3. 接着在你 clone 下来的文件目录中安装相关所需的 python 模块


		pip3 install -r requirements.txt

### 4. 接下来启动redis
		
		# 在redis安装目录下
		redis-server.exe  redis.windows.conf

		# 如果报这个错误 Creating Server TCP listening socket 127.0.0.1:6379: bind: No error
		# 运行一下命令
		redis-cli.exe
		127.0.0.1:6379>shutdown
		not connected>exit
		# 重新运行一下命令启动成功
		redis-server.exe redis.windows.conf

	当出现以下界面说明redis启动成功
		
		                _._
		           _.-``__ ''-._
		      _.-``    `.  `_.  ''-._           Redis 3.2.100 (00000000/0) 64 bit
		  .-`` .-```.  ```\/    _.,_ ''-._
		 (    '      ,       .-`  | `,    )     Running in standalone mode
		 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
		 |    `-._   `._    /     _.-'    |     PID: 11276
		  `-._    `-._  `-./  _.-'    _.-'
		 |`-._`-._    `-.__.-'    _.-'_.-'|
		 |    `-._`-._        _.-'_.-'    |           http://redis.io
		  `-._    `-._`-.__.-'_.-'    _.-'
		 |`-._`-._    `-.__.-'    _.-'_.-'|
		 |    `-._`-._        _.-'_.-'    |
		  `-._    `-._`-.__.-'_.-'    _.-'
		      `-._    `-.__.-'    _.-'
		          `-._        _.-'
		              `-.__.-'
		
		[11276] 27 Dec 22:02:24.986 # Server started, Redis version 3.2.100
		[11276] 27 Dec 22:02:25.012 * DB loaded from disk: 0.019 seconds
		[11276] 27 Dec 22:02:25.013 * The server is now ready to accept connections on port 6379
		
### 5. 接着就可以运行 run.py 了

		D:\git_project\proxy_pool\ProxyPool>run.py
		代理池开始运行
		 * Serving Flask app "proxypool.api" (lazy loading)
		 * Environment: production
		   WARNING: This is a development server. Do not use it in a production deployment.
		   Use a production WSGI server instead.
		 * Debug mode: off
		 * Running on http://0.0.0.0:5555/ (Press CTRL+C to quit)
		开始抓取代理
		获取器开始执行
		Crawling http://www.66ip.cn/1.html
		正在抓取 http://www.66ip.cn/1.html
		抓取成功 http://www.66ip.cn/1.html 200
		成功获取到代理 123.163.27.34:9999
		成功获取到代理 102.164.214.225:45528
		成功获取到代理 158.58.133.13:21213
		成功获取到代理 59.57.38.212:9999
		成功获取到代理 223.198.18.234:9999
		成功获取到代理 60.13.42.81:9999
		成功获取到代理 201.182.120.230:8080
		成功获取到代理 110.243.23.77:9999
		成功获取到代理 118.70.144.77:3128
		成功获取到代理 122.5.107.102:9999
		成功获取到代理 202.128.22.29:48678
		Crawling http://www.66ip.cn/2.html
		正在抓取 http://www.66ip.cn/2.html
		抓取成功 http://www.66ip.cn/2.html 200

抓到200的表示该代理可用

如果你在运行的时候出现这个错误
		
	AttributeError: 'int' object has no attribute 'items'
更新一下 redis 版本

	pip3 install redis==2.10.6 

运行 run.py 

这时候在你的 redis 中就有爬取到的代理 ip 了

也可以下载redis桌面软件[RedisDesktopManager](https://redisdesktop.com/subscriptions)

![RedisDesktopManager](https://i.imgur.com/0mYhE3P.png)



### 6.项目中使用
项目跑起来之后，你就可以访问你的代理池了

比如随机获取一个代理 ip 地址

	
	http://localhost:5555/random

这样访问之后就会获取到一个代理 ip，在代码中获取代理也不在话下啦
		
	
	import requests
	
	PROXY_POOL_URL = 'http://localhost:5555/random'
	
	def get_proxy():
	    try:
	        response = requests.get(PROXY_POOL_URL)
	        if response.status_code == 200:
	            return response.text
	    except ConnectionError:
	        return None