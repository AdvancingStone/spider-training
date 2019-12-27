from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import xlwt
from pathlib import Path
import os


# 有界面显示
# driver = webdriver.Chrome()
# driver.set_window_position(0, 0)
# driver.set_window_size(1400, 900)
# driver.maximize_window()#让窗口最大化

# 使用 PhantomJS 无声无息的操作各种动态网站（最新版本selenium弃用）
# driver = webdriver.PhantomJS()

# 使用以下三行代码可以不弹出界面，实现无界面爬取
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# options.binary_location=r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# 添加options参数， executable_path 可选，配置了环境变量后可省略，不然传该驱动的绝对路径
# driver = webdriver.Chrome(executable_path='chromedriver', options=options)# 配了环境变量第一个参数就可以省了，不然传绝对路径
driver = webdriver.Firefox(executable_path='geckodriver', options=options)  # 配了环境变量第一个参数就可以省了，不然传绝对路径

# 在抛出TimeoutException异常之前将等待10秒或者在10秒内发现了查找的元素。
# WebDriverWait 默认情况下会每500毫秒调用一次ExpectedCondition直到结果成功返回。
# ExpectedCondition成功的返回结果是一个布尔类型的true或是不为null的返回值。
WAIT = WebDriverWait(driver, 10)

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('周星驰', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '地址')
sheet.write(0, 2, '描述')
sheet.write(0, 3, '观看次数')
sheet.write(0, 4, '弹幕数')
sheet.write(0, 5, '发布时间')

n = 1


def search():
    try:
        print("开始访问B站...")
        driver.get("https://www.bilibili.com/")

        # 获取搜索框
        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#nav_searchform > .nav-search-keyword")))
        input.send_keys('周星驰 朱茵')
        input.send_keys(Keys.ENTER)

        # 跳转到新的窗口
        print('跳转到新窗口')

        all_handles = driver.window_handles
        driver.switch_to.window(all_handles[1])  # 选择新打开的窗口

        get_source()
        page_num = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.last > .pagination-btn'))).text
        # print(int(page_num))
        return int(page_num)

    except TimeoutException:
        return search()


def save_to_excel(soup):
    list = soup.find(class_='video-list').find_all(class_='video-item')
    for item in list:
        title = item.find('a').get('title')
        link = 'https:' + item.find('a').get('href')
        description = str(item.find(class_='des hide').text).strip()  # 描述
        view = str(item.find(class_='so-icon watch-num').text).strip()  # 观看次数
        biubiu = str(item.find(class_='so-icon hide').text).strip()  # 弹幕
        date = str(item.find(class_='so-icon time').text).strip()  # 上传时间

        print(title + '\t|' + link + '\t|' + description + '\t|' + view + '\t|' + biubiu + '\t|' + date)

        global n

        sheet.write(n, 0, title)
        sheet.write(n, 1, link)
        sheet.write(n, 2, description)
        sheet.write(n, 3, view)
        sheet.write(n, 4, biubiu)
        sheet.write(n, 5, date)

        n += 1


def get_source():
    WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.video-list > .video-item')))
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


def next_page(cur_page, page_num):

    print('当前页：'+str(cur_page) + '\t总页数：'+str(page_num))
    try:
        if cur_page <= page_num:
            next_btn = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.next')))
            # print(next_btn.text)
            next_btn.click()
            print('获取下一页数据')
        WAIT.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.active > .num-btn'), str(cur_page)))
        get_source()

    except TimeoutException:
        print("超时。。。。等待。。。。继续")
        driver.refresh()
        return next_page(page_num)


def main():
    try:
        page_num = search()
        print(page_num)

        for i in range(2, page_num + 1):
            next_page(i, page_num)

    finally:
        driver.close()


if __name__ == '__main__':
    main()
    url = 'D:\spider-fold\周星驰.xls'
    path = Path(url)
    if path.exists():
        os.remove(path)
    book.save(url)
