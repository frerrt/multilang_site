from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
import re
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate, gettext
from .models import Article

def home(request):
    welcome_msg = _('Welcome!')
    return render(request, 'home.html', {'msg': welcome_msg})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

responses = [
    _("Bonjour!"),
    _("Comment puis-je vous aider aujourd'hui?"),
    _("Cela semble intéressant. Parlez-moi plus de cela."),
    _("Je suis désolé, je ne comprends pas. Pouvez-vous reformuler?"),
    _("Bien sûr! Voici ce que je peux faire pour vous..."),
    _("Merci de me parler. Comment puis-je vous aider?"),
    _("Je pense que je peux vous aider avec ça!"),
]

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:chat')  # Redirect to chat after login
        else:
            return render(request, 'login.html', {'error': _('Invalid credentials')})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('main:login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def chat_view(request):
    return render(request, 'chat.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response = generate_response(user_message)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def generate_response(message):
    math_pattern = re.compile(r'^\s*([0-9\+\-\*/\(\)\s]+)\s*$')
    match = math_pattern.match(message)
    if match:
        try:
            result = eval(match.group(1), {"__builtins__": None}, {})
            return f"The answer is {result}"
        except Exception as e:
            return _("Sorry, I couldn't evaluate that expression.")
    
    if "help" in message.lower():
        return _("Sure, I'm here to help! What do you need assistance with?")
    elif "hello" in message.lower() or "hi" in message.lower():
        return random.choice([_("Hello!"), _("Hi there!"), _("Greetings!")])
    elif "name" in message.lower():
        return _("I'm your friendly chatbot.")
    else:
        return random.choice(responses)

def root_redirect(request):
    return redirect('main:home')
