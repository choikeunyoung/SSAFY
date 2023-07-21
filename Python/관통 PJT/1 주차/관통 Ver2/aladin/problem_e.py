import json


def new_books(books):
    books_info = {}
    for book in books:
        rep_word = book["id"]
        detail_info = open(f"data/books/{rep_word}.json", encoding="utf-8")
        detail_info = json.load(detail_info)
        books_info[rep_word] = (detail_info["title"], list(map(int,detail_info["pubDate"].split("-"))))
    
    Date_book = []
    
    for v in books_info.values():
        if v[1][0] == 2023:
            Date_book.append(v[0])

    return Date_book

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)
    
    print(new_books(books_list))
