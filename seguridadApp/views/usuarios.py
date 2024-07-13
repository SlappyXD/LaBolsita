from wsgiref.validate import validator
from django.forms import Form
from django.shortcuts import render, redirect
from typing import Generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User,Permission,Group
from django.core.paginator import Paginator
from django.db.models import Q 
from ventasApp.forms import UsuarioForm,UsuarioEditForm
from ventasApp.models import Categoria
from django.contrib.contenttypes.models import ContentType

#Funcion para "Gestionar Usuario"
def listarusuario(request):    
    queryset = request.GET.get("buscar")
    usuario = User.objects.all().filter( is_active=True).order_by('id').values()
    if queryset:
        usuario=User.objects.filter(Q(username__icontains=queryset)).filter( is_active=True).distinct().order_by('id').values()
    paginator = Paginator(usuario,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,"usuario/listar.html",{'page_obj': page_obj, 'usuarios':usuario})

# Función para "Nuevo Usuario"
def agregarusuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            username_user = form.cleaned_data.get("username")
            user_exists = User.objects.filter(username=username_user).exists()
            if user_exists:
                messages.info(request, "Username ya existe.")
                form = UsuarioForm()
                context = {'form': form}
                return render(request, "usuario/agregar.html", context)
            else:
                messages.success(request, "Usuario registrado.")
                user = User.objects.create_user(
                    username=form.cleaned_data.get("username"),
                    email=form.cleaned_data.get("email"),
                    password=form.cleaned_data.get("password")
                )
                user.is_superuser = form.cleaned_data.get("is_superuser")
                user.is_staff = form.cleaned_data.get("is_staff")
                user.is_active = form.cleaned_data.get("is_active")
                user.first_name = form.cleaned_data.get("first_name")
                user.last_name = form.cleaned_data.get("last_name")
                user.save()

                return redirect("listarusuario")
        else:
            messages.error(request, "El formulario no es válido. Por favor, revisa los datos ingresados.")
            context = {'form': form}
            return render(request, "usuario/agregar.html", context)
    else:
        form = UsuarioForm()
        context = {'form': form}
        return render(request, "usuario/agregar.html", context)

#Funcion para "Editar Usuario"
def editarusuario(request,id):
    user=User.objects.get(id=id)
    if request.method=="POST":
        form=UsuarioEditForm(request.POST)
        if form.is_valid():
            user.username = form.cleaned_data.get("username")
            user.email = form.cleaned_data.get("email")
            user.is_superuser = form.cleaned_data.get("is_superuser")
            user.is_staff = form.cleaned_data.get("is_staff")
            user.is_active = form.cleaned_data.get("is_active")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            messages.success(request, "Usuario actualizado.")
            return redirect("listarusuario") 
    else:
        initial_dict = {
            "last_name":user.last_name,"first_name":user.first_name,"email":user.email,
            "username":user.username,
            "is_superuser":user.is_superuser,"is_staff":user.is_staff,"is_active":user.is_active,
        }
        form=UsuarioEditForm(initial=initial_dict)
        context={"form":form} 
        return render(request,"usuario/editar.html",context)

#Funcion para "Eliminar Usuario"
def eliminarusuario(request,id):
    usuario=User.objects.get(id=id)    
    usuario.is_active=False
    usuario.eliminado=True
    usuario.save()
    messages.success(request, "User eliminado.")
    return redirect("listarusuario")

#Funcion para "Resetear contraseña Usuario"
def resetpasswordusuario(request,id):
    user=User.objects.get(id=id) 
    user.set_password('123')
    user.save()
    messages.success(request, "Contraseña de usuario reseteada a 123.")
    return redirect("listarusuario")

#Funcion para "Activar Usuario"
def activarusuario(request,id,activo):
    usuario=User.objects.get(id=id)
    if activo == 0:
        usuario.is_staff=True
    else:
        usuario.is_staff=False
    usuario.save()
    messages.success(request, "User actualizado.")
    return redirect("listarusuario") 