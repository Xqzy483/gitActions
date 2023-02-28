from bs4 import BeautifulSoup
from sphinx.util import requests


def crawl_baidu_top(board='realtime'):
    response = requests.get('https://top.baidu.com/board?tab={}'.format(board))
    soup = BeautifulSoup(response.text, 'html.parser')
    record_tags = soup.find_all('div', {'class': 'category-wrap_iQL oo'})
    titles, hot_indices = [], []
    for item in record_tags:
        title_tag = item.find('div', {'class': 'c-single-text-ellipsis'})
        hot_index_tag = item.find('div', {'class': 'hot-index_1Bl1a'})
        if (title_tag is not None) and (hot_index_tag is not None):
            titles.append(title_tag.text.strip())
            hot_indices.append(hot_index_tag.text.strip())
    return titles, hot_indices


if __name__ == '__main__':
    # crawl_baidu_top()
    print(crawl_baidu_top())
