from django.urls import path
from . import views


urlpatterns =[
    path("",views.opening,name='opening'),
    path("firstyear/",views.firstyear,name='firstyear'),
    path("kenken/",views.kenken,name="kenken"),
    path("slidepuzzle/",views.slidepuzzle,name="slidepuzzle"),
    path("slider/",views.slider,name="slider"),
    path("tangram/",views.tangram,name="tangram"),
    path("secondyear/",views.secondyear,name='secondyear'),
    path("thirdyear/",views.secondyear,name='thirdyear'),
    path("fourthyear/",views.secondyear,name='fourthyear'),
]

