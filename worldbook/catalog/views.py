from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Exists, OuterRef
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from jazzmin.templatetags.jazzmin import User

from .models import Book, Author, BookInstance, Genre, Subscription



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


def genre(request):
    genres = Genre.objects.all()
    return render(request, 'catalog/genre.html', {'genre': genres})


@login_required
@csrf_protect
def subscriptions(request):
    if request.method == 'POST':
        genre_id = request.POST.get('genre_id')
        genre = Genre.objects.get(id=genre_id)
        action = request.POST.get('action')

        if action == 'subscribe':
            Subscription.objects.create(user=request.user, genre=genre)
        elif action == 'unsubscribe':
            Subscription.objects.filter(
                user=request.user,
                genre=genre,
            ).delete()

    genre_with_subscriptions = Genre.objects.annotate(
        user_subscribed=Exists(
            Subscription.objects.filter(
                user=request.user,
            )
        )
    )
    return render(
        request,
        'catalog/subscriptions.html',
        {'genre': genre_with_subscriptions},
    )



class BookListView(ListView):
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



