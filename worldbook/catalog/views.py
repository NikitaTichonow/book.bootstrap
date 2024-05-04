from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Book, Author, BookInstance


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
    # Словарь для передачи данных в шаблон index.html
    context = {'text head': text_head,
               'books': books, 'num_books': num_books,
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors': authors, 'num_authors': num_authors}
    return render(request, 'catalog/index.html', context)


def about(request):
    text_head = 'Сведения о компании'
    name = '000 "Интелпектуальные информационные системы"'
    rab1 = 'Разработка приложений на основе', 'систем искусственного интелпекта'
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе', 'систем искусственного интелпекта'
    rab4 =  'Создание цифровых интерактивных книг, учебных пособий','автоматизированных обучающих систем'
    context = {'text head': text_head, 'name': name, 'rab1': rab1, 'rab2': rab2, 'rab3':rab3, 'rab4':rab4}
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы"'
    address = 'Москва, ул. Планерная, д. 20, к. 1'
    tel = '495-345-45-45'
    email = 'iis info@mail.ru'
    context = {'text _ head': text_head,'name': name, 'address': address, 'tel': tel, 'email': email}
    return render(request, 'catalog/contact.html', context)


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 4
    ordering = ['-id']


class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'


class AuthorListView(ListView):
    model = Author
    paginate_by = 4
    template_name = "catalog/author_list.html"
    ordering = ['-id']


class AuthorDetailView(DetailView):
    model = Author