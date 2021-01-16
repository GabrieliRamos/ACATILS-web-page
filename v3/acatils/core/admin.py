from django.contrib import admin

from .models import Categories, News

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'description', 'color', 'created', 'modified')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created', 'modified', 'slug')
