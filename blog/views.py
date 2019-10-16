from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


class PostList(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 3
