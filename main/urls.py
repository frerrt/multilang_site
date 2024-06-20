from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('item/',views.item,name='item'),
    path('',views.article_list,name='home'),
]