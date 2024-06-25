from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language,activate,gettext
from .models import Article
def home(request):
    welcome_msg = ('Welcome!')
    return render(request, 'home.html', {'msg': welcome_msg})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})