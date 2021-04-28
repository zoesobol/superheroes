from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from . import forms
from . import models
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect

# Create your views here.
class HomeView(generic.ListView):
    model = models.Superheroe
    template_name = 'home.html'
    ordering = ['-id']


class RegistroUsuario(generic.CreateView):
    form_class = forms.FormularioRegistro
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class LoginUsuario(auth_views.LoginView):
    form_class = forms.LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

def agregar_superheroe(request):
    if request.method == 'POST':
        form = forms.SuperheroeForm(request.POST,request.FILES or None)
        print('0')
        if form.is_valid():
            print("hola1")
            form.save(commit=False)
            print("hola2")
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print('false')
    else:
        form = forms.SuperheroeForm()
        context = {
            'form':form,
        }
    return render(request, 'agregar_superheroe.html', {'form':form})