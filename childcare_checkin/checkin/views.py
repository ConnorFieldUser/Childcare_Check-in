# from django.shortcuts import render
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from checkin.models import Child

from django.views.generic.edit import CreateView

# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class IndexView(TemplateView):
    template_name = 'index.html'


class ChildCreateView(CreateView):
    model = Child
    success_url = "/"
    fields = ('profile', 'first', 'last', 'pin')

    def form_valid(self, form):
        return super().form_valid(form)
