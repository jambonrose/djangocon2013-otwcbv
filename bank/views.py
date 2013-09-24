# bank/views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Account, Transaction
from .forms import TransferFormFrom, TransferFormTo

class AccountList(ListView):
    model = Account

    def get_context_data(self, **kwargs):
        context = super(AccountList, self).get_context_data(**kwargs)
        context['transaction_list'] = Transaction\
                                          .objects.order_by('-date')[:10]
        return context

class TransactionCreate(CreateView):
    model = Transaction

    def set_account(self, slug):
        account_obj = get_object_or_404(Account, slug__iexact=slug)
        self.acct_name = account_obj.name
        self.acct_pk = account_obj.pk
        self.acct_url = getattr(account_obj,'get_absolute_url', '')

    def get(self, request, *args, **kwargs):
        self.set_account(kwargs.get('slug', None))
        return super(TransactionCreate, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.set_account(kwargs.get('slug', None))
        return super(TransactionCreate, self).post(request, *args, **kwargs)

    def get_initial(self):
        initial_data = super(TransactionCreate, self).get_initial()
        if self.form_class == TransferFormFrom:
            initial_data['from_account'] = self.acct_pk
        elif self.form_class == TransferFormTo:
            initial_data['to_account'] = self.acct_pk
        else:
            raise ImproperlyConfigured(
                        '"form_class" variable must be defined '
                        'in %s for correct initial behavior.'
                        % (self.__class__.__name__, obj.__class__.__name__))
        return initial_data

    def get_context_data(self, **kwargs):
        context = {'account_name': self.acct_name}
        if self.form_class == TransferFormFrom:
            context['trans_dir'] = 'From:'
        elif self.form_class == TransferFormTo:
            context['trans_dir'] = 'To:'
        else:
            raise ImproperlyConfigured(
                        '"form_class" variable must be defined '
                        'in %s for correct initial behavior.'
                        % (self.__class__.__name__, obj.__class__.__name__))
        context.update(kwargs)
        return super(TransactionCreate, self).get_context_data(**context)

    def get_success_url(self):
        if (hasattr(self, 'acct_url') and self.acct_url != ''):
            return self.acct_url()
        else:
            return reverse('bank_account_list')
