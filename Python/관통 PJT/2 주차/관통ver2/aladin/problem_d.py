import requests
from pprint import pprint as print
import json

def author_other_works(title):
    # 검색 요청 API 확인해야함
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': 'ttbwwaall26261516002',
        'Query': title,
        'QueryType': 'Title',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
    }
    
    response = requests.get(URL, params=params).json()

    if response["item"] != []:
        author_info = list(response["item"][0]["author"].split("("))
        author_name = author_info[0]
        author_param = {
        'ttbkey': 'ttbwwaall26261516002',
        'Query': author_name,
        'QueryType': 'Author',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
        }

        res = requests.get(URL, params=author_param).json()
        answer_list = []
        for i in res["item"][:5]:
            answer_list.append(i["title"])
        return answer_list
    else:
        return None
    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(author_other_works('베니스의 상인'))

    print(author_other_works('개미'))

    print(author_other_works('*'))
