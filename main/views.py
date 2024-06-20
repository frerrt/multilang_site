from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language,activate,gettext
from .models import Article
def home(request):
    trans = translate(language='fr')
    return render(request, 'home.html', {'trans': trans})

def item(request):
    return render(request, 'item.html')

def article_list(request):
    # Determine the desired language, defaulting to 'en' if none is specified
    language = request.GET.get('lang', 'en')
    
    # Translate the articles' titles and contents
    articles = Article.objects.all()
    translated_articles = []
    for article in articles:
        translated_article = {
            'title': translate_text(article.title, language),
            'content': translate_text(article.content, language),
            'publication_date': article.publication_date
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
