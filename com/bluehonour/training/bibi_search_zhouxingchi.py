from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import xlwt


driver = webdriver.Chrome()
driver.set_window_position(0, 0)
driver.set_window_size(1400, 900)
# 在抛出TimeoutException异常之前将等待10秒或者在10秒内发现了查找的元素。
# WebDriverWait 默认情况下会每500毫秒调用一次ExpectedCondition直到结果成功返回。
# ExpectedCondition成功的返回结果是一个布尔类型的true或是不为null的返回值。
WAIT = WebDriverWait(driver, 10)

book = xlwt.Workbook(encoding='utf-8', style_compression=True)
sheet = book.add_sheet('')

def search():
    try:
        print("开始访问B站...")
        driver.get("https://www.bilibili.com/")

        # 获取搜索框
        input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-search-keyword")))
        input.send_keys('周星驰 朱茵')
        input.send_keys(Keys.ENTER)

        # 跳转到新的窗口
        print('跳转到新窗口')

        all_handles = driver.window_handles
        driver.switch_to.window(all_handles[1])  # 选择新打开的窗口

        get_source()
        page_num = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.last > .pagination-btn'))).text
        print(int(page_num))
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


def get_source():
    WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.video-list > .video-item')))
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


if __name__ == '__main__':
    page_num = search()
