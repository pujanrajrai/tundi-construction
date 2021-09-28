from django.contrib import auth
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.user.is_authenticated:
        # return redirect('dashboard:dashboard')
        return render(request, 'accounts/authenticate.html')
    if request.method == 'POST':
        if request.user.is_authenticated:
            return render(request, 'accounts/authenticate.html')
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'accounts/authenticate.html')

        else:
            errors = "User name or password is incorrect"
            return render(request, 'accounts/notauthenticate.html')

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'accounts/login.html')
