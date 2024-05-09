from django.contrib import admin

from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance
from django.utils.safestring import mark_safe


admin.site.site_title = 'Мир Книги - Администратирование'  # Изменяем название Админки в header
admin.site.site_header = 'Мир Книги - Администратирование'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'about', 'date_of_birth', 'get_image')
    fields = ['last_name', 'first_name', 'about', ('date_of_birth', 'photo'), 'get_image']
    readonly_fields = ('get_image',)  # Добавляем изображение в "Редактирование книг панель администратора"

    def get_image(self, obj):   # Скрипт вывода изображения обложки книги в панели администратора
        return mark_safe(f'<img src="{obj.photo.url}" width="80" height="100"')
    get_image.short_description = 'Изображение'


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'genre', 'language', 'get_image')
    list_filter = ('genre', 'author')
    readonly_fields = ('get_image',)  # Добавляем изображение в "Редактирование книг панель администратора"
    inlines = [BooksInstanceInline]
    def get_image(self, obj):   # Скрипт вывода изображения обложки книги в панели администратора
        return mark_safe(f'<img src="{obj.photo.url}" width="80" height="100"')
    get_image.short_description = 'Изображение'




admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)

