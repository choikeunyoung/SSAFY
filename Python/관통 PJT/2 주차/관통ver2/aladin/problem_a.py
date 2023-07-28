import requests
from pprint import pprint
import json
# 검색 요청 API 확인해야함
URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

params = {
    'ttbkey': 'ttbwwaall26261516002',
    'Query': '파울로 코엘료',
    'QueryType': 'Author',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

response = requests.get(URL, params=params).json()
# pprint(response["item"])
def author_works(res_info):
    book_lists = []
    for i in res_info:
        if "파울로 코엘료" in i["author"]:
            book_lists.append(i["title"])
    return book_lists


# # # 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(author_works(response["item"]))