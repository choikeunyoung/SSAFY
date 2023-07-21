import json


def best_new_books(books):
    books_info = {}
    for book in books:
        rep_word = book["id"]
        detail_info = open(f"data/books/{rep_word}.json", encoding="utf-8")
        detail_info = json.load(detail_info)
        books_info[rep_word] = (detail_info["title"], list(map(int,detail_info["pubDate"].split("-"))), detail_info["customerReviewRank"])
    
    max_value = 0
    max_id = 0

    for k,v in books_info.items():
        if v[1][0] == 2023:
            if v[2] >= max_value:
                max_id = k
                max_value = v[2]

    return books_info[max_id][0]



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(best_new_books(books_list))
