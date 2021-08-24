from authentication.forms import UserCreateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreateForm()

    return render(request, 'authentication/register.html', {'form': form})
