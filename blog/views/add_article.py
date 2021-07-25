from django.shortcuts import render, redirect

from blog.forms import AddArticleForm


def add_article(request):
    form = AddArticleForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save_m2m()
        return redirect('detail', slug=article.slug)
    return render(request, 'pages/add-article.html', context={
        'form': form
    })