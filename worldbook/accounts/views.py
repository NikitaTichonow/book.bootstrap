from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import CustomSignupForm


class SignUp(CreateView):
    model = User
    form_class = CustomSignupForm
    success_url = '/account/login'
    template_name = 'account/signup.html'


