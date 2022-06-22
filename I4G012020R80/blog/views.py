from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Post







class PostListView(ListView):
    model = Post
    templates = 'post_list.html'
  
      

class PostCreateView(CreateView):
    model = Post
    Fields = '__all__'
    templates = 'post_form.html'
    success_url  = reverse_lazy("blog:all")
    
class PostDetailView(DetailView):
    model = Post
    templates = 'post_detail.html'
    
class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    templates = 'post_form.html'
    success_url  = reverse_lazy("blog:all")
    
class  PostDeleteView(DeleteView):
    model = Post
    fields ='__all__'
    templates = 'post_confirm_delete.html'
    success_url  = reverse_lazy("blog:all")
       
    
    