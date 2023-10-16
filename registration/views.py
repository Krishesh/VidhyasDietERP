from django.shortcuts import render


# Create your views here.
def registration_list(request):
    context = {
        #'inquiry': Inquiry.objects.all().filter(trash=False)
    }
    return render(request, 'registration/registration_list.html', context)
