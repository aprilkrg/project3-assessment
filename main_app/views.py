from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List, Item

# from django.views.generic.edit import CreateView, DeleteView

# class ListCreate(CreateView):
#     model = List
#     fields = ['list_text']

#     def form_valid(self, form):
#         # Assign the logged in user (self.request.user)
#         form.instance.user = self.request.user
#         # Let the CreateView do its usual
#         return super().form_valid(form)

# class AddWish(CreateView):
#     model = List
#     fields = ['list_text']

def index(request):
    return render(request, 'main_app/index.html', {
        'items': Item.objects.all()
    })

def item_create(request):
    # return HttpResponse('hellooooooo world')
    # Item.objects.create(item_text=request.POST['item_text'])
    return render(request, 'item_create.html')
    # return redirect('index')