from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from blog.models import Post


# the function based view is to give a landing view and connect my work
def homeView(request):
    
    return render(request,'home.html')
    
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    success_url  = reverse_lazy("blog:all")
  
      



class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'post_form.html'
    success_url  = reverse_lazy("blog:all")
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'post_form.html'
    success_url  = reverse_lazy("blog:all")
    
class  PostDeleteView(DeleteView):
    model = Post
    fields ='__all__'
    template_name = 'post_confirm_delete.html'
    success_url  = reverse_lazy("blog:all")
       
    
    