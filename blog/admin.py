from django.contrib import admin

from blog.models import Category, Article, Comment, Contact

admin.site.register(Category)


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'detail')
    list_display = (
        'title', 'created_date', 'updated_date'
    )


class CommentAdmin(admin.ModelAdmin):
    search_fields = ('author__username',)
    list_display = (
        'author', 'created_date', 'updated_date'
    )


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display = (
        'email', 'created_date'
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)

