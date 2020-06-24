from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ListCreate.as_view(), name='index'),
    # path('add/', views.AddWish.as_view(), name='list'),

    path('', views.index, name='index'),
    path('add/', views.ItemCreate.as_view(), name='item_create'),
    path('delete/<int:item_id>', views.item_delete, name='item_delete'),
]