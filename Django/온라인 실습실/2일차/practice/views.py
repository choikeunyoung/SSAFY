from django.shortcuts import render

def price(request, menu, count):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if menu in product_price:
        context = {
            "menu" : menu,
            "price" : product_price[menu] * count,
            "cnt" : count,
        }
    else:
        context = {
            "menu" : menu,
            "price" : 0,
        }
    return render(request, "articles/price.html", context)