from django.urls import path
from . import views

urlpatterns = [
    path('all-articles',views.getArticles, name='all-articles'),
    path('add-article/',views.articleCreate, name='add-article'),
    path('add-room/',views.roomCreate, name='add-room'),
    path("item-detail/<str:pk>/", views.articleDetail, name ="item-detail"),
    path('article-update/<str:pk>/',views.articleUpdate, name='article-update'),
    path('article-delete/<str:pk>/',views.articleDelete, name='article-delete'),
    path('all-rooms',views.getRooms, name='all-rooms'),
    
]
