from django .urls import path

from blog.sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from . import views
from .feeds import LatestPostsFeed
app_name = 'blog'

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemaps'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag')

]
