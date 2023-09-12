from django.shortcuts import render
from . import data

# fruit_list = ["귤","딸기","사과","감","바나나","파인애플","구아바", "복숭아", "망고스틴"]
# hate = ["사과","구아바"]

# Create your views here.
def index(requests):
    contexts = {
        'fruit_list' : data.fruit_list,
        'hate' : data.hate,
    }
    return render(requests,"./articles/index.html", contexts)