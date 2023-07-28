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
def best_review_books(res_infos):
    res_list = []
    for res_info in res_infos:
        if res_info["customerReviewRank"] >= 9:
            res_list.append(res_info)

    return res_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(best_review_books(response['item']))
