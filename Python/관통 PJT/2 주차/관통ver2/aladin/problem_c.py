import requests
from pprint import pprint as print
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
def bestseller_book(res_infos):
    book_infos = sorted(res_infos, key = lambda x: x["salesPoint"], reverse=True)
    answer_list = []
    for book_info in book_infos[:5]:
        answer_list.append(book_info["title"])
    return answer_list



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(bestseller_book(response["item"]))

