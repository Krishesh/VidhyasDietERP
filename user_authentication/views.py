from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('index:index')
    else:

        if request.method == 'POST':
            email = request.POST.get('username')
            password = str(request.POST.get('password'))

            user = authenticate(request, username=email, password=password)
            print(email, password)
            if user is not None:
                login(request, user)

                return redirect('index:index')
            else:
                messages.info(request, 'USERNAME or PASSWORD is incorrect')

        context = {}
        return render(request, 'authentication/login.html',)


def logout_link(request):
    logout(request)
    return redirect('/login/')