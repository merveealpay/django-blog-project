from django import template
from blog.models import Category
from django import template

register = template.Library()


@register.simple_tag
def category_list():
    categories = Category.objects.all()
    return categories
