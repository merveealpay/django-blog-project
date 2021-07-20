from django.contrib import admin

from blog.models import Category, Article

admin.site.register(Category)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'detail')
    list_display = (
        'title', 'created_date', 'updated_date'
    )


admin.site.register(Article, ArticleAdmin)
