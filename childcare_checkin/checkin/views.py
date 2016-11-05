# from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from checkin.models import Child, Day

from django.views.generic.edit import CreateView

from django.http import HttpResponseRedirect

from django.urls import reverse

# Create your views here.


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class IndexView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        pin = request.POST["pin"]
        child = Child.objects.get(pin=pin)
        print(child)
        return HttpResponseRedirect(reverse("day_create_view"))
        # return HttpResponseRedirect(reverse("child_update_view", args=[child.id]))
        # return HttpResponseRedirect(reverse("child_detail_view", args=[child.id]))


class ChildCreateView(CreateView):
    model = Child
    success_url = "/"
    fields = ('profile', 'first', 'last', 'pin')


class DayCreateView(CreateView):
    model = Day
    success_url = "/"
    fields = ('hours',)


class ChildDetailView(DetailView):
    model = Child
