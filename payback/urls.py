from django.urls import path
from . import views


urlpatterns =[
    path("",views.opening,name='opening'),
    path("firstyear/",views.firstyear,name='firstyear'),
]