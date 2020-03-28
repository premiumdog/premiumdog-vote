from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('list/', views.article_top_list, name="article_top_list"),
    path('<slug:slug>/', views.article_details, name='article_details'),
    path('like', views.like_article, name='like_article'),
]