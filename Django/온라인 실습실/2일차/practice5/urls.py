from django.urls import path
from . import views

app_name = "practice5"

urlpatterns = [
        path("posts/", views.index, name="instargram"),
]
