from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book, name='create_book'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('', views.book_list, name='book_list'),
]
