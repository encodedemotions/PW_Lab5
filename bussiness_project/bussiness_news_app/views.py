from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Posts, AboutAuthor
from .forms import UserForm, PostForm, AboutAuthorForm


def index(request):

    post_objects = Posts.objects.all().order_by('id')[::-1]
    author_information = AboutAuthor.objects.all().order_by('id')

    context = {
        "is_authenticated": request.user.is_authenticated,
        "articles": post_objects,
        "authors_information": author_information
    }

    return render(request, 'bussiness_news_app/index.html', context)


def register(request):

    context = {}

    if request.method == 'POST':

        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')

            context['username'] = user_form.cleaned_data.get('username')

            user = authenticate(username=username, password=password)
            context['is_authenticated'] = user.is_authenticated
            context['user'] = user

            return render(request, 'registration/login.html', context)

    return render(request, 'bussiness_news_app/register.html')


@login_required()
def check_status(request):
    if request.user.is_staff:
        return redirect(request, 'bussiness_news_app/editor_page.html')


def editor_view(request):
    if request.method == 'POST':
        article_form = PostForm(data=request.POST, files=request.FILES)
        if article_form.is_valid():
            article_form = article_form.save(commit=False)
            article_form.save()
    return render(request, 'bussiness_news_app/editor_page.html')


def about_editor_view(request):
    if request.method == 'POST':
        about_author_form = AboutAuthorForm(data=request.POST, files=request.FILES)

        if about_author_form.is_valid():
            about_author_form = about_author_form.save(commit=False)
            about_author_form.save()

    return render(request, 'bussiness_news_app/about_page.html')


def search_view(request):

    if request.method == 'POST':

        if request.user.is_authenticated:
            articles_to_show = Posts(title=request.method['search'])
        else:
            articles_to_show = Posts(title=request.method['search'], article_permission='public')

        return render(request, 'bussiness_news_app/index.html', {'articles': articles_to_show})

    return render(request, 'bussiness_news_app/index.html')
