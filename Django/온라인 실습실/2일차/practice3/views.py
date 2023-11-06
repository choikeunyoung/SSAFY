from django.shortcuts import render

def first(request):
    if request.GET.get("order"):
        context = {
            "order" : request.GET.get("order"),
        }
        
    else:
        context = {
            "order" : "",
        }
    return render(request, "articles/first.html", context)


def second(request):
    if request.GET.get("order"):
        context = {
            "order" : request.GET.get("order"),
        }
        
    else:
        context = {
            "order" : "",
        }
    return render(request, "articles/second.html", context)


def third(request):
    if request.GET.get("order"):
        context = {
            "order" : request.GET.get("order"),
        }
        
    else:
        context = {
            "order" : "",
        }
    return render(request, "articles/third.html", context)