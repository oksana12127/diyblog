from django.contrib import admin
from django.contrib.auth.models import User


# Register your models here.
from .models import Comment, Blog, Bloger

# admin.site.register(Comment)
# admin.site.register(Blog)
# admin.site.register(Bloger)

# Define the admin class
class BlogerAdmin(admin.ModelAdmin):
    list_display = ('bloger_name', 'nik_name','bio')


# Register the admin class with the associated model
admin.site.register(Bloger, BlogerAdmin)

# Register the Admin classes for Book using the decorator

class CommentInline(admin.TabularInline):
    model = Comment



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # inlines = [CommentInline]
    inlines = [CommentInline]

# @admin.register(Nik)
# class BlogAdmin(admin.ModelAdmin):
#     pass

# Register the Admin classes for BookInstance using the decorator

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'summary', 'moment', 'blog_comment']


# Создайте пользователя и сохраните его в базе данных

# @admin.register(Author)
# class AuthorAdmin(admin.ModelAdmin):
#     plist_display = ( 'author' )