from django.shortcuts import render
from Autos.models import *
from Autos.forms import *
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, "Autos/index.html")

class MostrarAuto(ListView):
    model = Auto

class BuscarAuto(ListView):
    model = Auto
    context_object_name = "autos"

    def get_queryset(self):
        f = BuscarAutoForm(self.request.GET)
        if f.is_valid():
            return Auto.objects.filter(marca__icontains=f.data["criterio_auto"]).all
        return Auto.objects.none()
    
class AutoDetail(DetailView):
    model = Auto
    
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    success_url = reverse_lazy("auto-list")
    fields = '__all__'

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    success_url = reverse_lazy("auto-list")
    fields = '__all__'

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = reverse_lazy("auto-list")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('auto-list')

class LogIn(LoginView):
    pass

class LogOut(LogoutView):
    template_name = 'registration/logout.html'