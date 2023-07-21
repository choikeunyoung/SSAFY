import json
from pprint import pprint as print


def best_book(books):
    books_info = {}
    for book in books:
        rep_word = book["id"]
        detail_info = open(f"data/books/{rep_word}.json", encoding="utf-8")
        detail_info = json.load(detail_info)
        books_info[rep_word] = (detail_info["title"], detail_info["customerReviewRank"])
    
    max_id = 0
    max_value = 0.0

    for k,v in books_info.items():
        if v[1] >= max_value:
            max_value = v[1]
            max_id = k
    
    return books_info[max_id][0]

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_book(books_list))
