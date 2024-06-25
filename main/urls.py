from django.urls import path,include

from . import views

app_name = 'main'

urlpatterns = [
    path('',views.article_list,name='home'),
    path('chat/', include('chatbot.urls')),
]