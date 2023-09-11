from django.shortcuts import render

# Create your views here.
def inquiry_list(request):
    return render(request, 'inquiry/inquiry_list.html')


def add_inquiry(request):
    return render(request, 'inquiry/add_inquiry.html')