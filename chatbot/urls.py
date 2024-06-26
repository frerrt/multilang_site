# chatbot/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('chat/', views.chat_view, name='chat'),  # Add chat view
    path('chatbot-response/', views.chatbot_response, name='chatbot_response'),  # Add chatbot response view
]
        