from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListCreate.as_view(), name='index'),
    path('list/create', views.list_create, name='list_create',),

]