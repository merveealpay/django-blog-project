from django.shortcuts import render, get_object_or_404

from blog.models import Article


def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comments = article.comments.all()
    return render(request, 'pages/detail.html', context={
        'article': article,
        'comments': comments
    })
