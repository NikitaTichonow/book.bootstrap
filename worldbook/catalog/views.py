from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from rest_framework.response import Response
from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import permissions
from .serializers import *
from .models import *



def index(request):
    text_head = 'На нашем сайте вы можете nолучить книги в электронном виде'
    # Данные о книгах и их количестве
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'На складе')
    num_instances_available = BookInstance.objects.filter(status__exact='2').count()
    # Данные об авторах книг
    authors = Author.objects
    num_authors = Author.objects.count()
    # Количество посещений этого view, подсчитанное в переменной session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Словарь для передачи данных в шаблон index.html
    context = {'text head': text_head,
               'books': books, 'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors': authors, 'num_authors': num_authors, 'num_visits': num_visits}
    return render(request, 'catalog/index.html', context)


def about(request):
    text_head = 'Сведения о компании'
    name = '000 "Интелпектуальные информационные системы"'
    rab1 = 'Разработка приложений на основе', 'систем искусственного интелпекта'
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе', 'систем искусственного интелпекта'
    rab4 = 'Создание цифровых интерактивных книг, учебных пособий', 'автоматизированных обучающих систем'
    context = {'text head': text_head, 'name': name, 'rab1': rab1, 'rab2': rab2, 'rab3': rab3, 'rab4': rab4}
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы"'
    address = 'Москва, ул. Планерная, д. 20, к. 1'
    tel = '495-345-45-45'
    email = 'iis info@mail.ru'
    context = {'text _ head': text_head, 'name': name, 'address': address, 'tel': tel, 'email': email}
    return render(request, 'catalog/contact.html', context)



class GenreListView(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Genre
    template_name = 'catalog/genre.html'


# def genre(request):
#     genres = Genre.objects.all()
#     serializer_class = GenreSerializer
#     return render(request, 'catalog/genre.html', {'genre': genres})


class BookListView(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Book
    context_object_name = 'books'
    paginate_by = 4
    ordering = ['-id']


class BookDetailView(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Book
    context_object_name = 'book'


class AuthorListView(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Author
    paginate_by = 4
    template_name = "catalog/author_list.html"
    ordering = ['-id']


class AuthorDetailView(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Author


class AuthorsAPIView(generics.ListAPIView):
   queryset = Author.objects.all()
   serializer_class = AuthorsSerializer
   permission_classes = [permissions.IsAuthenticated]

class BooksAPIView(generics.ListAPIView):
   queryset = Book.objects.all()
   serializer_class = BooksSerializer
   permission_classes = [permissions.IsAuthenticated]

class GenresAPIView(generics.ListAPIView):
   queryset = Genre.objects.all()
   serializer_class = GenresSerializer
   permission_classes = [permissions.IsAuthenticated]

class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



# Обработка ошибок
def tr_handler404(request, exception):
    """
    Обработка ошибки 404
    """
    return render(request=request, template_name='403.html', status=404, context={
        'title': 'Страница не найдена: 404',
        'error_message': 'К сожалению такая страница была не найдена, или перемещена',
    })


def tr_handler500(request):
    """
    Обработка ошибки 500
    """
    return render(request=request, template_name='403.html', status=500, context={
        'title': 'Ошибка сервера: 500',
        'error_message': 'Внутренняя ошибка сайта, вернитесь на главную страницу, отчет об ошибке мы направим администрации сайта',
    })


def tr_handler403(request, exception):
    """
    Обработка ошибки 403
    """
    return render(request=request, template_name='403.html', status=403, context={
        'title': 'Ошибка доступа: 403',
        'error_message': 'Доступ к этой странице ограничен',
    })


def tr_handler400(request, exception):
    """
    Обработка ошибки 400
    """
    return render(request=request, template_name='403.html', status=403, context={
        'title': 'Ошибка доступа: 400',
        'error_message': 'Упс !!! Кажется у нас проблемы на сервере!!!',
    })