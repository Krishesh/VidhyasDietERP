from django.shortcuts import render
from django.contrib.auth import logout
# Create your views here.
def index(request):

    return render(request, 'index/index.html')