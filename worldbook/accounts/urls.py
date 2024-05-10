from django.urls import path
from . import views
from .views import SignUp

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),

]