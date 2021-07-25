from django.urls import path
from blog.views import contact, index, category, my_articles, detail, add_article

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    path('category/<slug:categorySlug>', category, name='category'),
    path('my-articles', my_articles, name='my_articles'),
    path('detail/<slug:slug>', detail, name='detail'),
    path('add-article', add_article, name='add_article'),

]