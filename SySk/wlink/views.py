from django.shortcuts import render, redirect
from .models import Link, Categoria

from .forms import RegLinkModelForm, RegCategoriaModelForm
# Create your views here.



def registrarCategoria(request):
    titulo = "Registrar Categoria"
    form = RegCategoriaModelForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        categoria = form.cleaned_data.get("categoria")
        descripcion = form.cleaned_data.get("descripcion")

        instance.save()
        
    context = {
        'titulo': titulo,
        'form': form,
    }
    return render(request, "registrarCategoria.html", context)


def eliminar(request, id_link):
    link = Link.objects.get(id=id_link)
    
    if request.method == 'POST':  
        link.delete()
        return redirect('inicio')
        
    context = {
        'link': link,
    }
    return render(request, "eliminar.html", context)




def registrar(request):
    titulo = "Registrar Links"
    form = RegLinkModelForm(request.POST or None) 
    
    if form.is_valid():
        instance = form.save(commit=False)
        web = form.cleaned_data.get("web")
        link = form.cleaned_data.get("link")
        categoria = form.cleaned_data.get("categoria")
        
        instance.save()    
        return redirect('inicio')
        
    context = {
        'titulo': titulo,
        'form': form,
    }
    return render(request, "registrar.html", context)

def perfil(request):
    titulo = "perfil"
    context = {
        "titulo": titulo,
    }
    return render(request, "perfil.html", context)
    
def login(request):
    titulo = "Login"
    context = {
        "titulo": titulo,
    }
    return render(request, "login.html", context)
        
def inicio(request):
    titulo = "Bienvenido"
    form = RegLinkModelForm(request.POST or None)
    lst_links = Link.objects.all()
    
    context = {
        "lst_links": lst_links,
        "titulo": titulo,
    }
    return render(request, "inicio.html",context)

def portada(request):
    titulo = "SySK"
    
    context = {
        "titulo": titulo,
    }
    return render(request, "portada.html", context)














