import json
from pprint import pprint


def book_info(book, categories):
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
    return book_dict
    # 여기에 코드를 작성합니다.  

        


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
