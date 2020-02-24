from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('snipt/', views.snipt_form, name='snipt'),
]
