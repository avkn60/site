from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/', views.news_page, name='news_page'),
    path('news/detail/<int:pk>/', views.news_detail_page, name='news_detail_page'),
]