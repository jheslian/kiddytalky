from django.shortcuts import render


def my_account_view(request):
    return render(request, 'myAccount.html')