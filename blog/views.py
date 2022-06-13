from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 1)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {
        'posts': posts,
        'page': page
    })


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published',)

    return render(request, 'blog/post/detail.html', {'post': post})
