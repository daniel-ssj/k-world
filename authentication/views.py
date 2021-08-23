from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            context = {
                'error': 'Username and password cannot be blank'
            }

            return render(request, 'authentication/login.html', context)

        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {
                'error': 'Wrong username or password'
            }

            return render(request, 'authentication/login.html', context)

        login(request, user)

        return redirect('/')

    return render(request, 'authentication/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

    if not username or not password:
        context['error'] = 'Username and password cannot be blank'

        return render(request, 'authentication/login.html', context)

    if password != password_confirm:
        context['error'] = 'Password mismatch'

        return render(request, 'authentication/login.html', context)

    User.objects.create(username=username, password=password)

    user = authenticate(request, username=username, password=password)

    login(request, user)

    return render(request, 'authentication/register.html', {})
