# bank/views.py
from django.views.generic import ListView
from .models import Account, Transaction

class AccountList(ListView):
    model = Account

    def get_context_data(self, **kwargs):
        context = super(AccountList, self).get_context_data(**kwargs)
        context['transaction_list'] = Transaction\
                                          .objects.order_by('-date')[:10]
        return context
