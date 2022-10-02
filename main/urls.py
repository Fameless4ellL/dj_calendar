from django.template.defaulttags import url
from django.urls import path, re_path

from . import views

urlpatterns = [
    path(r"", views.index, name='index'),
    path(r"date_<int:year>_<int:month>", views.index, name='index'),
]