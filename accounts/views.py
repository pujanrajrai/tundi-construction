from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard:home')
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('dashboard:home')
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard:home')
        else:
            context = {"errors": "User name or password is incorrect"}
            return render(request, 'accounts/login.html', context)
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'accounts/login.html')
