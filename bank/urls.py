# bank/urls.py
from django.conf.urls import patterns, url
from .models import Account
from .views import (AccountList, AccountDetail,
                   AccountCreate, TransactionCreate)

urlpatterns = patterns('',
    url(r'^account/$',
        AccountList.as_view(),
        name='bank_account_list'),
    url(r'^account/create/$',
        AccountCreate.as_view(),
        name='bank_account_create'),
    url(r'^account/(?P<slug>[\w\-]+)/$',
        AccountDetail.as_view(),
        name='bank_account_detail'),
    url(r'^transaction/$',
        TransactionCreate.as_view(),
        name='bank_trans_create'),
)
