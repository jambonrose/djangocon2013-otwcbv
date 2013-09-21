# bank/views.py
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from .models import Account
from .forms import AccountForm, TransactionForm

class AccountList(View):
    def get(self, request):
        acct_list = Account.objects.all()
        return render(request,
                      'bank/account_list.html',
                      {'account_list': acct_list})

class AccountDetail(View):
    def get(self, request, slug):
        acct = get_object_or_404(Account, slug=slug)
        return render(request, 'bank/account_detail.html', {'account': acct})

class AccountCreate(View):
    def get(self, request):
        form = AccountForm()
        return render(request, 'bank/account_form.html', {'form': form})

    def post(self, request):
        form = AccountForm(request.POST)
        if form.is_valid():
            new_acct = form.save()
            return redirect(new_acct)
        else:
            return render(request, 'bank/account_form.html', {'form': form})

class TransactionCreate(View):
    def get(self, request):
        form = TransactionForm()
        return render(request, 'bank/account_form.html', {'form': form})

    def post(self, request):
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_acct = form.save()
            return redirect('bank_account_list')
        else:
            return render(request, 'bank/account_form.html', {'form': form})
