from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import re
from django.utils.translation import gettext_lazy as _
from .models import Article
import random


def home(request):
    welcome_msg = _('Welcome!')
    return render(request, 'home.html', {'msg': welcome_msg})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

responses = [
    "Bonjour!",
    "Comment puis-je vous aider aujourd'hui?",
    "Cela semble intéressant. Parlez-moi plus de cela.",
    "Je suis désolé, je ne comprends pas. Pouvez-vous reformuler?",
    "Bien sûr! Voici ce que je peux faire pour vous...",
    "Merci de me parler. Comment puis-je vous aider?",
    "Je pense que je peux vous aider avec ça!",
]

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')  # Redirect to chat after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def chat_view(request):
    return render(request, 'chat.html')

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        # Process the user message and generate a response
        response = generate_response(user_message)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def generate_response(message):
    # Check if the message contains a mathematical expression
    math_pattern = re.compile(r'^\s*([0-9\+\-\*/\(\)\s]+)\s*$')
    match = math_pattern.match(message)
    
    if match:
        try:
            # Safely evaluate the mathematical expression
            result = eval(match.group(1), {"__builtins__": None}, {})
            return f"The answer is {result}"
        except Exception as e:
            return "Sorry, I couldn't evaluate that expression."

    # Basic keyword-based response logic
    if "help" in message.lower():
        return "Sure, I'm here to help! What do you need assistance with?"
    elif "hello" in message.lower() or "hi" in message.lower():
        return random.choice(["Hello!", "Hi there!", "Greetings!"])
    elif "name" in message.lower():
        return "I'm your friendly chatbot."
    else:
        # Return a random response from the predefined list
        return random.choice(responses)