from django.shortcuts import redirect, render
from .forms import UsuarioForm

# Create your views here.
def cadastrar_usuario(request):
    if request.method =="POST":
         form_usuario = UsuarioForm(request.POST)
         if form_usuario.is_valid():
             form_usuario.save()
             return redirect('index')
            
    else:         
        form_usuario = UsuarioForm()
    return render(request, 'form_usuario.html', {'form_usuario': form_usuario})

