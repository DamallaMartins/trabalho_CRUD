from django.urls import path
from . import views

urlpatterns = [
    path('', views.filme, name='filme'),
    path('novo/', views.criar_filme, name='criar_filme'),
    path('<int:pk>/editar/', views.editar_filme, name='editar_filme'),
    path('<int:pk>/excluir/', views.excluir_filme, name='excluir_filme'),
]