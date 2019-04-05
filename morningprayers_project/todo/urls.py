from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_todo', views.show_todo, name='show_todo'),
    # path(r'^todo/(?P<id>[\w\-]+)/$', views.show_todo, name='show_todo'),
]

