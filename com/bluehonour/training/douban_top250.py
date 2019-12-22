import requests
import re
from bs4 import BeautifulSoup
import xlwt
from pathlib import Path
import os

# 代理池
proxy_pool_url = {
    'http': '103.28.57.122:8080',
    'http': '36.66.209.3:8080',
    'http': '111.79.44.184:9999',
    'http': '114.239.149.110:9999',
    'http': '117.69.200.216:9999',
    'http': '123.160.1.150:9999'
}

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '排名')
sheet.write(0, 1, '名称')
sheet.write(0, 2, '评分')
sheet.write(0, 3, '评论次数')
sheet.write(0, 4, '描述')
sheet.write(0, 5, '导演')
sheet.write(0, 6, '主演')
sheet.write(0, 7, '年份')
sheet.write(0, 8, '地区')
sheet.write(0, 9, '类别')
sheet.write(0, 10, '图片')

n = 1


def request_douban(url, headers, proxies):
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        print(response.status_code)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def save_to_excel(soup):
    li_items = soup.select('.grid_view li')  # 获取class="grid_view"下的所有li标签（逐层查找）
    for item in li_items:
        movie_title = item.select_one('.hd > a > span').string  # 电影名
        img_addr = item.select_one('img')['src']  # 图片地址
        rank = item.select_one('.pic > em').string  # 排名
        grade = item.select_one('.star > .rating_num').string  # 评分
        comments_num = item.select('.star > span')[3].string[:-3]  # 评论次数
        description = item.select_one('.quote > .inq').string  # 描述
        details = item.select_one('.bd > p')  # .children  #获取导演，主演，年份，地区，类别
        line1 = details.next_element
        line2 = line1.next_element.next_element
        print(str(line1).strip())
        # maker = ''  # 导演
        # protagonist ='' # 主演
        try:
            pattern = re.compile('导演: (.*?)主演: (.*)', re.S)
            content = re.match(pattern, str(line1).strip())
            maker = content.group(1).strip()    # 导演
            protagonist = content.group(2).strip()[:-3]     # 主演
        except Exception:
            maker = ''
            protagonist = ''
        pattern2 = re.compile('(.*)/(.*)/(.*)')
        content2 = re.match(pattern2, str(line2).strip())
        year = content2.group(1).strip()  # 年份
        country = content2.group(2).strip()  # 地区
        catagory = content2.group(3).strip()  # 类别
        print(rank + '|' + movie_title + '|' + grade + '|' + comments_num + '|' + description + '|' + maker + '|' +
            protagonist + '|' + year + '|' + country + '|' + catagory + '|' + img_addr)

        global n
        sheet.write(n, 0, rank)
        sheet.write(n, 1, movie_title)
        sheet.write(n, 2, grade)
        sheet.write(n, 3, comments_num)
        sheet.write(n, 4, description)
        sheet.write(n, 5, maker)
        sheet.write(n, 6, protagonist)
        sheet.write(n, 7, year)
        sheet.write(n, 8, country)
        sheet.write(n, 9, catagory)
        sheet.write(n, 10, img_addr)

        n = n + 1


def main(page, path, flag):

    if flag and path.exists():
        os.remove(path)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/72.0.3626.121 Safari/537.36 '
    }
    for i in range(0, page):
        url = 'https://movie.douban.com/top250?start=' + str(i * 25) + '&filter='
        html = request_douban(url, headers=headers, proxies=proxy_pool_url)
        soup = BeautifulSoup(html, 'lxml')
        save_to_excel(soup)


if __name__ == "__main__":
    filename = 'D:\spider-fold\电影.xls'
    path = Path(filename)
    main(10, path, True)
    book.save(path)