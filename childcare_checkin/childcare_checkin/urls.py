"""childcare_checkin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from checkin.views import UserCreateView, IndexView, ChildCreateView, ChildDetailView, ChildListView, DayCreateView, DayUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^create_child$', ChildCreateView.as_view(), name="child_create_view"),
    url(r'^child/(?P<pk>\d+)/$', ChildDetailView.as_view(), name="child_detail_view"),
    url(r'^child/(?P<pk>\d+)/create$', DayCreateView.as_view(), name="day_create_view"),
    url(r'^day/(?P<pk>\d+)/update$', DayUpdateView.as_view(), name="day_update_view"),
    url(r'^childs/$', ChildListView.as_view(), name="child_list_view")
]
