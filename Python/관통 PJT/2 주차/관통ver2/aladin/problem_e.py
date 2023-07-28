import requests
from pprint import pprint as print
import json

def ebook_list(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    book_params = {
        'ttbkey': 'ttbwwaall26261516002',
        'Query': title,
        'QueryType': 'Title',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'Book',
        'output' : 'js',
        'Version' : '20131101'
    }


    ebook_params = {
        'ttbkey': 'ttbwwaall26261516002',
        'Query': title,
        'QueryType': 'Title',
        'MaxResults' : 20,
        'start' : 1,
        'SearchTarget' : 'eBook',
        'output' : 'js',
        'Version' : '20131101'
    }

    book_response = requests.get(URL, params=book_params).json()
    ebook_response = requests.get(URL, params=ebook_params).json()
    if book_response["item"] == [] or ebook_response["item"] == []:
        return None
    
    book_response = book_response["item"][0]
    ebook_response = ebook_response["item"][0]
    
    book_price = book_response["priceSales"] 
    ebook_price = ebook_response["priceSales"]
    book_price = int(book_price - (book_price*(10**-1)))

    answer_list = []
    if ebook_price < book_price:
        answer_dict = {}
        answer_dict["isbn"] = ebook_response["isbn"]
        answer_dict["itemId"] = ebook_response["itemId"]
        answer_dict["link"] = ebook_response["link"]
        answer_dict["priceSales"] = ebook_response["priceSales"]
        answer_list.append(answer_dict)
    return answer_list

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(ebook_list('베니스의 상인'))

    print(ebook_list('*'))
