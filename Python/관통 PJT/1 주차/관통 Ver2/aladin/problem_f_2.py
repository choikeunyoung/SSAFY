import json


def sorted_cs_books_by_price(books, categories):
    id_number = 0
    for v in categories:
        if v["name"] == "컴퓨터 공학":
            id_number = v["id"]
    
    cate_books = []
    
    for book in books:
        if id_number in book["categoryId"]:
            cate_books.append(book["title"])

    return cate_books
    
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
