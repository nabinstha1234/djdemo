from django.urls import path
from crud import views

urlpatterns = [
    path('', views.emp, name='home1'),
    path('show/', views.show, name='show'),
]
