# bank/urls.py
from django.conf.urls import patterns, url
from .models import Account
from .views import (account_list, account_detail,
                    account_create, transaction_create)

urlpatterns = patterns('',
    url(r'^account/$',
        account_list,
        name='bank_account_list'),
    url(r'^account/create/$',
        account_create,
        name='bank_account_create'),
    url(r'^account/(?P<slug>[\w\-]+)/$',
        account_detail,
        name='bank_account_detail'),
    url(r'^transaction/$',
        transaction_create,
        name='bank_trans_create'),
)
