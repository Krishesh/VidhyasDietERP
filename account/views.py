from django.shortcuts import render

from account.models import Account


# Create your views here.
def account_list(request):
    context = {
        'account': Account.objects.all(),
    }
    return render(request, 'account/account_list.html', context)
