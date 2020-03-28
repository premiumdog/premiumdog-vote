from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserRegisterForm
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from gallery.models import Gallery
from django.core.paginator import Paginator
from .models import Donation, Gdpr, Join
from django.contrib.auth import authenticate, login

# Create your views here.

def homepage(request):
    donation = Donation.objects.last()
    articles = Article.objects.annotate(like_count = Count('likes')).exclude(group__in=['Hobby', 'FCI által nem elismert kutyafajták']).order_by('-like_count')[:3]
    articles_hobby = Article.objects.annotate(like_count = Count('likes')).filter(group='Hobby').order_by('-like_count')[:3]
    articles_not_fci = Article.objects.annotate(like_count = Count('likes')).filter(group='FCI által nem elismert kutyafajták').order_by('-like_count')[:3]
    return render(request, 'static/homepage.html', {'articles': articles, 'donation':donation,'articles_hobby':articles_hobby, 'articles_not_fci':articles_not_fci})

def tutorial(request):
    return render(request, 'static/tutorial.html')


def gdpr(request):
    gdpr = Gdpr.objects.last()
    return render(request, 'static/gdpr.html',{'gdpr':gdpr})

def join(request):
    article = Join.objects.last()
    return render(request, 'static/join.html',{'article':article})


def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 32)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/article_list.html', {'articles':articles, 'page_obj': page_obj})



def article_details(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    gallery = article.gallery.all()
    total_likes = article.likes.count()
    is_liked = False
    if article.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'article':article,
        'gallery':gallery,
        'total_likes':total_likes,
        'is_liked':is_liked,}
    return render(request, 'articles/article_details.html', context)

def article_top_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_top_list.html', {'articles':articles})



def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Gratulálunk, sikeresen létrehozta a profilját. Most már leadhatja a szavazatait!')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})


def like_article(request):
    article = get_object_or_404(Article, id=request.POST.get('teszt'))
    article.likes.add(request.user)
    messages.success(request, 'Gratulálunk, Ön sikeresen szavazott! Adja le további szavazatait is.')
    return redirect('homepage')

"""
def custom_register(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!{username}')
            return redirect('login')
    else:
        form = CustomForm()
    return render(request, 'registration/register.html', {'form':form})
"""