from django.shortcuts import render
from Autos.models import *
from Autos.forms import *
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, "Autos/about.html")

def index(request):
    context = {
        'publicaciones': Auto.objects.all()
    }
    return render(request, "Autos/index.html", context)

class MostrarAuto(ListView):
    model = Auto

def BuscarAuto(request):
    busqueda = request.GET.get("buscar")
    autos = Auto.objects.all()

    if busqueda:
        autos = Auto.objects.filter(
            Q(marca__icontains= busqueda) |
            Q(modelo__icontains= busqueda) |
            Q(año__icontains= busqueda) |
            Q(color__icontains= busqueda)
        ).all()
    return render(request, 'Autos/search.html', {'autos':autos})
        
class AutoDetail(DetailView):
    model = Auto
    
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    success_url = reverse_lazy("auto-list")
    fields = '__all__'

class AutoUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Auto
    success_url = reverse_lazy("auto-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Auto.objects.filter(dueño=user_id, id=post_id,).exists() 
    
    def handle_no_permission(self):
        return render(self.request, "Autos/not_found_post.html")

class AutoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Auto
    success_url = reverse_lazy("auto-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Auto.objects.filter(dueño=user_id, id=post_id,).exists()

    def handle_no_permission(self):
        return render(self.request, "Autos/not_found_post.html")

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy('mensaje-list')

class MostrarMensaje(ListView):
    model = Mensaje

class MensajeDetail(DetailView):
    model = Mensaje

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id, id=post_id,).exists()

    def handle_no_permission(self):
        return render(self.request, "Autos/not_found_mensaje.html")

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy("index")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id,).exists() 
    
    def handle_no_permission(self):
        return render(self.request, "Autos/not_found_user.html")

class ProfileDetail(DetailView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile
    success_url = reverse_lazy("login")
    fields = '__all__'
    
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('profile-create')

class LogIn(LoginView):
    pass

class LogOut(LogoutView):
    template_name = 'registration/logout.html'