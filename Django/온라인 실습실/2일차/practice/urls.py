from django.urls import path
from . import views

urlpatterns = [
        path("price/<str:menu>/<int:count>/", views.price, name="price"),
]
