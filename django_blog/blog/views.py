from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.shortcuts import render, redirect
# Create your views here.

def register_view(request):
    if request.method ==  'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form" : form})
