from django.urls import path
from .views import SignUp
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
]