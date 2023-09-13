from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("throw/", views.throw, name="throw"),
    path("catch/", views.catch, name="catch"),
    path("number/<int:num>/", views.detail, name="detail"),
    path("hello/<str:name>/", views.greeting, name="greeting"),
]
