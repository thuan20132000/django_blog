from django.contrib import admin

from blog.models import Comment, Menu, Post, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# Apply summernote to all TextField in model.


@admin.register(Post)
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    summernote_fields = '__all__'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


@admin.register(Menu)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
