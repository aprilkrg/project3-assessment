from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ListCreate.as_view(), name='index'),
    # path('add/', views.AddWish.as_view(), name='list'),

    path('', views.index, name='index'),
    path('add/', views.item_create, name='item_create'),

]