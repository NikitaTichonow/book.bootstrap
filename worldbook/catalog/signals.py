from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Book, Subscription


@receiver(m2m_changed, sender=Book)
def book_created(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.genre).values_list('email', flat=True)

    subject = f'Новый товар в жанре {instance.genre_id}'

    text_content = (
        f'Товар: {instance.name}\n'
        f'Ссылка на товар: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Товар: {instance.name}<br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на книигу</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, "None", [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

