from django.urls import path
<<<<<<< HEAD

urlpatterns = [
    path("practice2/", include("practice2.urls")),
=======
from . import views

urlpatterns = [
        path("calculator/<int:first>/<int:second>/", views.calculator, name="calculator"),
>>>>>>> 4ff1a4d2cac770954257085ccc84c1545f075687
]
