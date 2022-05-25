from django.urls import path
from . import views

urlpatterns= [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('', views.sair, name='sair_logout'),

]