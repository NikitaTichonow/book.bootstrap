from django.urls import path
from .import views

app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('genre/', views.genre, name='genre'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('<str:username>/', views.UserProfileView.as_view(), name='user_profile'),

]