from .models import *
from rest_framework import serializers



class AuthorsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ['id', 'last_name', 'first_name', 'date_of_birth', 'about']


class BooksSerializer(serializers.ModelSerializer):
   class Meta:
       model = Book
       fields = ['id', 'title', 'genre', 'language', 'publisher', 'price', 'isbn', 'summary']


class GenresSerializer(serializers.ModelSerializer):
   class Meta:
       model = Genre
       fields = ['id', 'name', 'about']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']