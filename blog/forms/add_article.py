from django import forms

from blog.models import Article


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author', 'slug')