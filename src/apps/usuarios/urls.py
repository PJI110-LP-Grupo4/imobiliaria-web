from django.urls import path
from .views import cadastrar_usuario

urlpatterns = [
    path('cadastrar_usuario', cadastrar_usuario, name='cadastrar_usuario'),
    
]