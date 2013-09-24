# bank/urls.py
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Account, Transaction
from .forms import AccountForm, TransferFormFrom, TransferFormTo
from .views import AccountList, TransactionCreate

urlpatterns = patterns('',
    url(r'^account/$',
        AccountList.as_view(),
        name='bank_account_list'),
    url(r'^account/create/$',
        CreateView.as_view(model=Account,
                           form_class=AccountForm),
        name='bank_account_create'),
    url(r'^account/(?P<slug>[\w\-]+)/$',
        DetailView.as_view(model=Account),
        name='bank_account_detail'),
    url(r'^transaction/$',
        CreateView.as_view(model=Transaction,
                           success_url=reverse_lazy('bank_account_list')),
        name='bank_trans_create'),
    url(r'^account/from/(?P<slug>[\w\-]+)/$',
        TransactionCreate.as_view(form_class=TransferFormFrom),
        name='bank_trans_from'),
    url(r'^account/to/(?P<slug>[\w\-]+)/$',
        TransactionCreate.as_view(form_class=TransferFormTo),
        name='bank_trans_to'),
)
