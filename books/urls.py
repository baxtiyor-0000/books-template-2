from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('my-books/', views.my_books, name='my_books'),
    path('book/<int:pk>/share/', views.share_book, name='share_book'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]