from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import *
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
@csrf_protect
def user_login(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user is not None and user.check_password(password):
            login(request, user)
            return redirect('index')
        else:
            if user is None:
                messages.error(request, 'Username does not exist.')
            else:
                messages.error(request, 'Incorrect password.')

    return render(request, 'login.html', {'page': page})

def user_logout(request):
    logout(request)
    return redirect('login')