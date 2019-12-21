import requests
import json
from bs4 import BeautifulSoup
from pathlib import Path
import os


def request_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


# 正则狗臭屁慢死了（跑不出来）
'''
def parse_result(html):
    pattern = re.compile(
        '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">¥(.*?)</span>.*?</li>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'range': item[0], #排名
            'iamge': item[1], #图片地址
            'title': item[2], #书名
            'recommend': item[3],#推荐指数
            'author': item[4], #作者
            'times': item[5],#五星评分次数
            'price': item[6] #价格
        }
'''


# 使用BeautifulSoup
def parse_result(html):
    bs = BeautifulSoup(html, 'lxml')
    ul_item = bs.find('ul', class_='bang_list clearfix bang_list_mode')
    li_items = ul_item.find_all('li')
    for item in li_items:
        publisher_info_item = item.find_all(class_='publisher_info')
        author_list = publisher_info_item[0].find_all('a')  # 作者可能有多个
        author = ''
        for x in author_list:
            author = author + x.string + '&'  # 使用 & 分割不同作者
        # author = author[:-1]
        price_item = item.find(class_='price')
        e_book = item.find(class_='price_e').find('span', class_='price_n')  # 判断是否为None
        if e_book is not None:
            e_book_price = e_book.string
        else:
            e_book_price = ''
        yield {
            'list_num': item.find('div', class_='list_num').string[0:3],  # 书清单号
            'book_name': item.find('div', class_='name').find('a')['title'],  # 书名
            'pict_addr': item.find(class_='pic').find('a').find('img')['src'],  # 图片地址
            'comments': item.find(class_='star').find('a').string[:-3],  # 评论数
            'rate': item.find(class_='star').find('span', class_='tuijian').string,  # 推荐指数
            'author': author[:-1],  # 作者
            'publish_date': publisher_info_item[1].find('span').string,  # 出版时间
            'publishing_house': publisher_info_item[1].find('a').string,  # 出版社
            'five_stat_num': item.find(class_='biaosheng').find('span').string[:-1],  # 五星评分次数
            'original_price': price_item.find(class_='price_r').string,  # 原价
            'now_price': price_item.find(class_='price_n').string,  # 现价
            'discount': price_item.find(class_='price_s').string,  # 折扣
            'e_book_price': e_book_price  # 电子书价钱
        }


'''
    item: 要写的内容
    path：文件路径
    mode: w覆盖写，a追加写
'''


def write_item_to_file(item, path, mode):
    print('开始写入数据 ====> ' + str(item))
    with open(path, mode, encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


'''
    page: 页数
    flag: 是否删除文件
'''


def main(page, flag):
    for i in range(1, page):
        url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(i)
        html = request_dangdang(url)
        items = parse_result(html)  # 解析过滤我们想要的信息
        path = Path('D:\\spider-fold\\book.txt')
        if flag and path.exists():
            os.remove(path)
            flag = False
        for item in items:
            write_item_to_file(item, path, 'a')


if __name__ == "__main__":
    main(26, True)
