from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import EmailMultiAlternatives, mail_admins, mail_managers
from django.contrib.auth.models import User


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Ваше имя')
    last_name = forms.CharField(max_length=30, label='Ваша фамилия')

    def save(self, request):
        user = super().save(request)

        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)

        subject = 'Добро пожаловать в наш интернет-магазин!'
        text = f'{user.username}, вы успешно зарегистрировались на сайте!'
        html = (
            f'<b>{user.username}</b>, вы успешно зарегистрировались на '
            f'<a href="http://127.0.0.1:8000/products">сайте</a>!'
        )
        msg = EmailMultiAlternatives(
            subject=subject, body=text, from_email=None, to=[user.email]
        )
        msg.attach_alternative(html, "text/html")
        msg.send()

        mail_managers(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        mail_admins(
            subject='Новый пользователь!',
            message=f'Пользователь {user.username} зарегистрировался на сайте.'
        )

        return user
