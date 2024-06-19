from django.shortcuts import render, redirect
from .models import Article
from django.utils.translation import activate,get_language
from django.views.decorators.csrf import csrf_protect

def csrf_failure(request, reason=""):
    return render(request, 'csrf_failure.html', {"reason": reason})

def article_list(request):
    lang_code = request.GET.get('lang', None)
    if lang_code:
        activate(lang_code)
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'LANGUAGE_CODE': get_language()
    }
    return render(request, 'article_list.html', context)

@csrf_protect
def set_language(request):
    if request.method == 'POST':
        lang_code = request.POST.get('language')
        if lang_code:
            activate(lang_code)
            request.session['django_language'] = lang_code
        return redirect(request.POST.get('next', '/'))
    return redirect('/')