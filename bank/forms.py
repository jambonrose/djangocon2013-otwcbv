# bank/forms.py
from django.forms import ModelForm
from .models import Account, Transaction

class AccountForm(ModelForm):
    class Meta:
        model = Account

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
