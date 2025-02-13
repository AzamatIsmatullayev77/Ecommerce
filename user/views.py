from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import messages


# Create your views here.

def simple_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('ecommerce:index')
            else:
                messages.add_message(request,
                                     messages.ERROR,
                                     'Username or password is incorrect')
    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context=context)


def simple_logout(request):
    logout(request)
    return render(request, 'user/logout.html')


def register(request):
    return render(request, 'user/register.html')


def forgot_password(request):
    return render(request, 'user/forgot-password.html')
