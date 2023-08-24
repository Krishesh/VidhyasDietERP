from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import logout


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
                print(messages)

        context = {}
        return render(request, 'authentication/login.html', )


def logout_page(request):
    logout(request)
    return render(request, 'authentication/login.html', )
