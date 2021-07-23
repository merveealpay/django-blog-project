from django.urls import path
from blog.views import contact, index, category

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact),
    path('category/<slug:categorySlug>', category, name='category'),
]