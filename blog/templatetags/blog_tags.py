from django import template
from blog.models import Menu, Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
from taggit.models import Tag

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


@register.simple_tag
def get_similar_posts(post, count=5):

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(
        tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count(
        'tags')).order_by('-same_tags', '-publish')[:4]

    return similar_posts


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_latest_posts(count=4):
    return Post.published.order_by('-publish')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def get_menus():
    return Menu.published.all()


@register.simple_tag
def get_all_tags():

    tags = Tag.objects.annotate(post_num=Count('post')).order_by('-post_num').all()
    
    # return tags(
    #     total_comments=Count('comments')
    # ).order_by('-total_comments')[:count]
    return tags
