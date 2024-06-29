from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.article_list, name='articles'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('chat/', views.chat_view, name='chat'),
    path('chatbot-response/', views.chatbot_response, name='chatbot-response'),
]
