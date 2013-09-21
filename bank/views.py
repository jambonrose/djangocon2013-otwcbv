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

class FormMixin(object):
    form = None
    template = ''
    redirect = ''

    def get(self, request):
        form = self.form()
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            new_obj = form.save()
            if self.redirect:
                return redirect(self.redirect)
            else:
                return redirect(new_obj)
        else:
            return render(request, self.template, {'form': form})

class AccountCreate(FormMixin, View):
    form = AccountForm
    template = 'bank/account_form.html'

class TransactionCreate(FormMixin, View):
    form = TransactionForm
    template = 'bank/account_form.html'
    redirect = 'bank_account_list'
