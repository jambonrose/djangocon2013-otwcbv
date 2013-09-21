# bank/views.py
from django.shortcuts import get_object_or_404, redirect, render
from .models import Account
from .forms import AccountForm, TransactionForm

def account_list(request):
    acct_list = Account.objects.all()
    return render(request,
                  'bank/account_list.html',
                  {'account_list': acct_list})

def account_detail(request, slug):
    acct = get_object_or_404(Account, slug=slug)
    return render(request,
                  'bank/account_detail.html',
                  {'account': acct})

def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            new_acct = form.save()
            return redirect(new_acct)
    else:
        form = AccountForm()
    return render(request,
                  'bank/account_form.html',
                  {'form': form})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_trans = form.save()
            return redirect('bank_account_list')
    else:
        form = TransactionForm()
    return render(request,
                  'bank/transaction_form.html',
                  {'form': form})
