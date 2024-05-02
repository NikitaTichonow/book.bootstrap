from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text_head = 'Это заголовок главной страницы сайта'
    text_body = 'Это содержимое главной страницы сайта'
    context = {'text_head': text_head, 'text_body': text_body}
    return render(request, 'catalog/index.html', context)