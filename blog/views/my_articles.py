from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


@login_required(login_url='/')
def my_articles(request):
    articles = request.user.articles.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(articles, 2)
    return render(request, 'pages/my_articles.html', context={
        'articles': paginator.get_page(page),
    })
