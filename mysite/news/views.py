from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm
from django.urls import reverse_lazy
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin  # Миксин для ограничения доступа к разделам сайта.


def test(request):


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name: str = 'news'
    #extra_context = {'title': 'Главная'}
    mixin_prop = 'hello world'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')
        # .select_related('category'), работает со связью foreign key
        # prefetch_related - работает со связью many to many,
        # методы грузят связанные данные не отложенно а жадно

class ViewNews(DetailView):
    model = News
    #pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


"""
def index(request):
    news = News.objects.all()

    context = {
        'news': news,
        'title': 'Список новостей',

    }
    return render(request, 'news/index.html', context)
"""


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False  #  не выводить категорию если она пуста (заперет показа пустого списка)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news,

                                                  'category': category })


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    #success_url =  reverse_lazy('home')  # куда редиректить после создания новости
    # если этого метода нет, тогда редирект происходить через метод models.get_absolute_url
    raise_exception = True




# def view_news(request, news_id):
#     #news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item} )  # второй параметр название шаблона который рендерится


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)  # обращаемся к объекту equest и забираем у него POST
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#
#     return render(request, 'news/add_news.html', {'form': form})