from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    """Класс для того, какие поля показывать в админке"""
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_field = ('title', 'content')  # искать по этому полю
    list_editable = ('is_published',)  # редактировать это поле в меню админки
    list_filter = ('is_published', 'category')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')  # какие поля из предыдушего не редактируемы
    save_on_top = True

    # метод для вывода картинки в админке
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'Миниатюра'  # что бы переименовать название колонки в админке

class CategoryAdmin(admin.ModelAdmin):
    """Класс для того, какие поля показывать в админке"""
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_field = ('title',)  # здесь должен быть кортеж, поэтому запятая в конце


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
