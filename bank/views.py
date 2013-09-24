# bank/views.py
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Account, Transaction

class AccountList(ListView):
    model = Account

class AccountDetail(DetailView):
    model = Account

class AccountCreate(CreateView):
    model = Account

class TransactionCreate(CreateView):
    model = Transaction
    success_url = reverse_lazy('bank_account_list')
