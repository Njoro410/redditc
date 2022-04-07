from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('add/',views.articleCreate, name='add-article'),
    path("item-detail/<str:pk>/", views.articleDetail, name ="item-detail"),
    path('article-update/<str:pk>/',views.articleUpdate, name='article-update'),
    path('article-delete/<str:pk>/',views.articleDelete, name='article-delete'),
]
