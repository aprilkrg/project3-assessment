from django.shortcuts import render, redirect
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import List

# Create your views here.
# class ListCreate(CreateView):
#     model = List

def home(request):
    return render(request, 'main_app/index.html', {
        'list': List.objects.all()
    })

def list_create(request):
    List.objects.create(list_text=request.POST['list_text'])
    return redirect('index')