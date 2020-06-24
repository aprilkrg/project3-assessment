from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List, Item

from django.views.generic.edit import CreateView, DeleteView

class ItemCreate(CreateView):
    model = Item
    fields = ['item_text']
    success_url = '/'

# class AddWish(CreateView):
#     model = List
#     fields = ['list_text']

def index(request):
    return render(request, 'main_app/index.html', {
        'items': Item.objects.all()
    })

def item_create(request):
    print(request.POST)
    Item.objects.create(request.POST)
    return render(request, 'item_create.html')

def item_delete(request, item_id):
    Item.objects.filter(id=item_id).delete()
    return redirect('index')
    
