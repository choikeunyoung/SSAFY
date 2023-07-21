import json
from pprint import pprint


def books_info(books, categories):
    books_list = []
    for book in books:
        book_dict = {}
        book_dict["id"] = book["id"]
        book_dict["title"] = book["title"]
        book_dict["author"] = book["author"]
        book_dict["priceSales"] = book["priceSales"]
        book_dict["description"] = book["description"]
        book_dict["cover"] = book["cover"]
        book_dict["categoryName"] = book["categoryId"]
        append_list = []
        for i in book_dict["categoryName"]:
            for j in categories:
                if j["id"] == i:
                    append_list.append(j["name"])
        book_dict["categoryName"] = append_list
        books_list.append(book_dict)
    return books_list
        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))