from django.urls import path, include
from . import views

urlpatterns=[
	path('accounts/', include('django.contrib.auth.urls')),
    path('books/<int:pk>/', views.book_detail, name='book_detail'), 
    path('books/', views.book_index, name='book_index'), 
    path('authors/<int:pk>/', views.author_detail, name='author_detail'), 
    path('authors/', views.author_index, name='author_index'), 
    path('genres/<int:pk>/', views.genre_detail, name='genre_detail'), 
    path('genres/', views.genre_index, name='genre_index'), 
    path('users/<int:pk>/', views.user_detail, name='user_detail'), 
    path('register/', views.register, name='register'), 

]