from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_word$', views.random_word)
]