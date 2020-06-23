from django.contrib import admin
from .models import Article, Comment


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display= ('id','title','content')
class CommentAdmin(admin.ModelAdmin):
    list_display= ('id','article_id','content')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment,CommentAdmin)