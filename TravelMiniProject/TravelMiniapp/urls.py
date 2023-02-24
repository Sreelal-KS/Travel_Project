from . import views
from django.urls import path

urlpatterns = [

    # path('', views.firstview, name='first')
    # path('', views.home, name='home')
    path('', views.index, name='index')
]