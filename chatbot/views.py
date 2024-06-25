# chatbot/views.py
from django.shortcuts import render
import random

responses = [
    "Bonjour!",
    "Comment puis-je vous aider aujourd'hui?",
    "Cela semble intéressant. Parlez-moi plus de cela.",
    "Je suis désolé, je ne comprends pas. Pouvez-vous reformuler?",
    "Bien sûr! Voici ce que je peux faire pour vous...",
    "Merci de me parler. Comment puis-je vous aider?",
    "Je pense que je peux vous aider avec ça!",
]

def chatbot(request):
    return render(request, 'chatbot.html')
