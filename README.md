# multilang_site
Assurez-vous d'avoir les éléments suivants installés :

    Python 3.6+
    Django 3.0+
    Pip pour installer les bibliothèques Python nécessaires

Installation

    Clonez le dépôt :

    bash

git clone https://github.com/frerrt/multilang_site.git
cd multilang_site

Créez et activez un environnement virtuel :

bash

python -m venv venv
source venv/bin/activate  

Installez les dépendances nécessaires :

bash

    pip install -r requirements.txt
    pip install -r requirements.txt -U


pour lancer le serveur: python manage.py runserver

partie chatbot:

Description

Cette application Django intègre un simple chatbot pour fournir des réponses basiques prédéfinies.
Prérequis


Configuration du Projet

    Créez les modèles pour les documents dans chat/models.py :

    python

# chat/models.py
from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

Créez les vues pour le chatbot dans chat/views.py :

python

# chat/views.py
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
    if request.method == 'POST':
        user_input = request.POST.get('message')
        random_response = random.choice(responses)
        return JsonResponse({'response': random_response})
    return render(request, 'chatbot.html')

Créez les templates dans chat/templates :

    chatbot.html :

    html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Chatbot</title>
        <script>
            async function sendMessage() {
                const message = document.getElementById('message').value;
                const response = await fetch("{% url 'chatbot' %}", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'X-CSRFToken': '{{ csrf_token }}'
                    },
                    body: new URLSearchParams({'message': message})
                });
                const data = await response.json();
                document.getElementById('response').innerText = data.response;
            }
        </script>
    </head>
    <body>
        <h1>Chatbot</h1>
        <input type="text" id="message">
        <button onclick="sendMessage()">Send</button>
        <p id="response"></p>
    </body>
    </html>

Mettez à jour les URLs dans chat/urls.py :

python

# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
]

Incluez ces URLs dans le fichier principal urls.py :

python

    # myproject/urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('chat/', include('chat.urls')),
    ]

Exécution du Projet

    Appliquez les migrations et démarrez le serveur :

    bash

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

    Accédez à http://127.0.0.1:8000/fr/chat/ pour interagir avec le chatbot.



