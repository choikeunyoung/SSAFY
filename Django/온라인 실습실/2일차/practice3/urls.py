from django.urls import path
from . import views

app_name = "practice2_2"

urlpatterns = [
    path("first/", views.first, name="first"),
    path("second/", views.second, name="second"),
    path("third/", views.third, name="third"),
]
