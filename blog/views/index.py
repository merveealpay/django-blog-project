from django.db.models import Q
from django.shortcuts import render
from blog.models import Category, Article
from django.core.paginator import Paginator


def index(request):
    query = request.GET.get('query')
    articles = Article.objects.order_by('-id')

    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(detail__icontains=query)
        ).distinct()

    page = request.GET.get('page')
    paginator = Paginator(articles, 2)

    return render(request, 'pages/index.html', context={
        'articles': paginator.get_page(page)
    })
