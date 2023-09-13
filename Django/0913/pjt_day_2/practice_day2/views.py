from django.shortcuts import render

def index(request):
    context = {
        "name": "Kc"
    }
    return render(request, "articles/index.html", context)


# def choice(request):
#     context = {
        
#     }

def search(request):
    return render(request, "articles/search.html")

def throw(request):
    return render(request, 'articles/throw.html')
    
def catch(request):
    message = request.GET.get("message")
    context = {
        "message" : message,
    }
    return render(request, 'articles/catch.html', context)

def detail(request, num):
    return render(request, "articles/detail.html", { "num" : num })

def greeting(request, name):
    return render(request, "articles/greeting.html", { "name" : name })