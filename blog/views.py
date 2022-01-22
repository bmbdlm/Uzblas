from django.shortcuts import render
from django.views import generic
from .models import Post

def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html',{'posts':posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    return render(request, 'blog/post_detail.html', {'post': post})

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'templates/index.html'

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'templates/post_detail.html'

# Create your views here.
