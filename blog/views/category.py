from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from blog.models import Article, Category


def category(request, categorySlug):

    category = get_object_or_404(Category, slug=categorySlug)
    articles = category.article.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(articles, 2)
    return render(request, 'pages/category.html', context={
        'articles': paginator.get_page(page),
        'category_name': category.name
    })
