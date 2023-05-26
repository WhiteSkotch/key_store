from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import MyUserCreationForm, MyAuthenticationForm

def registration(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def log(request):
    if request.method == 'POST':
        form = MyAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = MyAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'lk.html')