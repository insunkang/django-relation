from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Article,Comment
from .forms import ArticleForm,CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    # comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form':comment_form,
        # 'comments':comments
    }
    return render(request, 'articles/detail.html', context)
@login_required
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES) # form : forms.ModelForm > ArticleForm 클래스의 instance
        if form.is_valid():
            article = form.save(commit=False) # article : models.Model > Article 클래스의 instance
            article.user = request.user
            article.save()
            messages.success(request,'게시글 작성 완료')
            return redirect('articles:detail', article.pk)
        else:
            messages.error(request,'잘못된 데이터를 넣었따')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)
@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
        else:
            return redirect('articles:detail', article.pk)
    return redirect('articles:detail', article.pk)

@login_required
def comment(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # comment = get_object_or_404(Comment, pk=article_pk)
    # comment = Comment.objects.get(article_id=article_pk)
    # article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article 
            comment.user = request.user
            comment.save()
            # comment.content = request.POST.get('content')
            # comment.save()
            return redirect('articles:detail', article.pk)
    else:
        form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

@require_POST
def comment_delete(request, article_pk,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    else:
        pass

    return redirect('articles:detail', article_pk)

