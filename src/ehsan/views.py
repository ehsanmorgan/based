from django.shortcuts import render

# Create your views here.
from .models import post


from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
class postList(ListView):
    model=post



class postDetai(DetailView):
    model=post


class postCreate(CreateView):
    model=post
    fields=['title','content']
    success_url=('/blog/')


class postUpdate(UpdateView):
    model=post
    fields=['title','content']
    success_url=('/blog/')



class postDelete(DeleteView):
    model=post
    fields=['title','content']
    success_url=('/blog/')