from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from main import views
urlpatterns = [
    path('', views.article_list, name='article_list'),  
    path('admin/', admin.site.urls),
    path('setlang/', views.set_language, name='set_language'),
]

