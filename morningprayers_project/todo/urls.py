from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('show_todo', views.show_todo, name='show_todo'),
    # path(r'^todo/(?P<id>[\w\-]+)/$', views.show_todo, name='show_todo'),
    path ('show_todo/<slug:slug>',views.show_todo, name='show_todo'),
    path ('add_todo', views.add_todo, name='add_todo'),
    path ('modify_todo/<slug:slug>',views.modify_todo, name='modify_todo'),
]

