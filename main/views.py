from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language,activate,gettext
from .models import Article
def home(request):
    welcome_msg = ('Welcome!')
    return render(request, 'home.html', {'msg': welcome_msg})

def item(request):
    return render(request, 'item.html')

def article_list(request):
    language = get_language()
    
    articles = Article.objects.all()
    translated_articles = []
    
    for article in articles:
        if language == 'en':
            translated_title = article.title_en or article.title
            translated_content = article.content_en or article.content
        elif language == 'fr':
            translated_title = article.title_fr or article.title
            translated_content = article.content_fr or article.content
        else:
            # Default to original language (fallback)
            translated_title = article.title
            translated_content = article.content
        
        translated_article = {
            'title': translated_title,
            'content': translated_content,
            'published_date': article.published_date,
        }
        translated_articles.append(translated_article)
    
    return render(request, 'home.html', {'articles': translated_articles})

def translate_text(text, language):
    cur_language = get_language()
    try:
        activate(language)
        translated_text = gettext(text)
    finally:
        activate(cur_language)
    return translated_text

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text
