from django.urls import path,include

from . import views

app_name = 'main'

urlpatterns = [
    path('',views.article_list,name='home'),
    path('articles/',views.article_list,name='articles'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('chatbot/', views.chat_view, name='chat'),  # Add chat view
    path('chatbot-response/', views.chatbot_response, name='chatbot-response')
]