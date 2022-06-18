from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    """Класс для того, какие поля показывать в админке"""
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_field = ('title', 'content')  # искать по этому полю
    list_editable = ('is_published',)  # редактировать это поле в меню админки
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    """Класс для того, какие поля показывать в админке"""
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_field = ('title',)  # здесь должен быть кортеж, поэтому запятая в конце


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
