from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
=======
def calculator(request, first, second):
    multiply = first*second
    if second != 0:
        division = first/second
    else:
        division = 0
    minous = first-second
    context = {
        "first" : first,
        "second" : second,
        "multiply" : multiply,
        "division" : division,
        "minous" : minous,
    }
    return render(request, "articles/calculator.html", context)
>>>>>>> 4ff1a4d2cac770954257085ccc84c1545f075687
