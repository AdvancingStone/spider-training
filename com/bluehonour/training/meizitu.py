import requests
from bs4 import BeautifulSoup
import os
import time
import concurrent
from concurrent.futures import ThreadPoolExecutor

# 代理池
proxy_pool_url = {
    'http': '103.28.57.122:8080',
    'http': '36.66.209.3:8080',
    'http': '111.79.44.184:9999',
    'http': '114.239.149.110:9999',
    'http': '117.69.200.216:9999',
    'http': '123.160.1.150:9999'
}
# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
    "Referer": "https://www.mzitu.com/xinggan/"
}


def request_page(url):
    try:
        response = requests.get(url, headers=headers, proxies=proxy_pool_url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


# 返回总页数
def request_homepage(url):
    content = request_page(url)
    if content is not None:
        soup = BeautifulSoup(content, 'lxml')
        page_num = soup.select('.nav-links > a')[-2].string  # 页数
        print('总页数：' + str(page_num))

        # get_page_url_and_title(url)
        return int(page_num)


# 找到每个页面中的二级图片地址和标题
def get_page_url_and_title(url):
    content = request_page(url)
    if content is not None:
        soup = BeautifulSoup(content, 'lxml')
        ul_item = soup.select_one('.postlist > #pins')
        li_list = ul_item.select('li')
        list = []
        for li in li_list:
            pic_url = li.select_one('a').get('href')  # 二级图片地址
            # print(pic_addr)
            title = li.select_one('img').get('alt')  # 标题
            # print(title)
            list.append((pic_url, title))
        return (list)


def download_all_pic(path, pic_list):
    """

    :param path: 路径
    :param pic_list: pic_url and title
    :return:
    """
    # pic_num = pic_list.__len__

    for pic_url, title in pic_list:
        print(pic_url + '\t' + title)
        same_title_pic_num = get_pic_num(pic_url)
        print('same_title_pic_num: ' + str(same_title_pic_num))

        if same_title_pic_num is not None:

            sub_path = path + '/' + title
            isExists =  os.path.exists(sub_path)
            if not isExists:
                os.mkdir(sub_path)

            download_pic(sub_path + '/1.jpg' , pic_url)
            for i in range(2, same_title_pic_num+1):
                download_pic(sub_path + '/' + str(i) + '.jpg', pic_url + '/' + str(i))
                time.sleep(0.5)


# 返回同一个title图片的数量
def get_pic_num(url):
    content = request_page(url)
    if content is not None:
        soup = BeautifulSoup(content, 'lxml')
        page_num = int(soup.select('.pagenavi > a')[-2].string)
        # print(int(page_num))  # 图片数量
        return page_num
    return None


# 下载图片到指定文件夹
# https://www.mzitu.com/201793
def download_pic(absolute_path, pic_url):
    print('absolute_path: ' + absolute_path)
    print("pic_url: "+pic_url)

    content = request_page(pic_url)
    if content is not None:
        soup = BeautifulSoup(content, 'lxml')
        a_tag = soup.select_one('.main-image > p >a > img')
        # print(a_tag)
        img_src = a_tag.get('src')
        # print(img_src)

        with open(absolute_path, 'wb') as f:
            img = requests.get(img_src, headers=headers).content
            print('download----------------' + img_src)
            f.write(img)
            f.close()




if __name__ == "__main__":

    url = 'https://www.mzitu.com/'
    total_page_num = request_homepage(url)
    # 使用多线程在这里为什么设置为1，因为超过1 有些图片不能下载。。。请求太快，服务器不给响应
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as exector:
        for i in range(1, total_page_num+1):
            list = get_page_url_and_title(url + 'page/' + str(i))
            exector.submit(download_all_pic, 'D:\spider-fold\meizitu', list)



