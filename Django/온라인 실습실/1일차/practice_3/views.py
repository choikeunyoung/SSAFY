from django.shortcuts import render

age = range(25,31)
grade = ['a','b','c','s']

def certification1(request):
    context = {
    'name' : "baegopa",
    'age' : age,
    'grade' : grade,
    }

    return render(request, "articles/certification1.html", context)


def certification2(request):
    context = {
    'name' : "nedoo",
    'age' : age,
    'grade' : grade,
    }
    return render(request, "articles/certification2.html", context)


def certification3(request):
    context = {
    'name' : "nadoo",
    'age' : age,
    'grade' : grade,
    }
    return render(request, "articles/certification3.html", context)