# bank/models.py
from django.db import models
from django.db.models import Q
from django.core.urlresolvers import reverse

class Account(models.Model):
    name = models.CharField('Account Name', max_length=127)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    balance = models.IntegerField('Balance')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bank_account_detail',
                       kwargs={'slug': self.slug})

    def get_trans_from_url(self):
        return reverse('bank_trans_from',
                       kwargs={'slug':self.slug})

    def get_trans_to_url(self):
        return reverse('bank_trans_to',
                       kwargs={'slug':self.slug})

    def related_transactions(self):
        return Transaction._default_manager.filter(Q(from_account=self) |
                                                   Q(to_account=self))\
                                           .order_by('-date')

class Transaction(models.Model):
    amount = models.IntegerField('Amount')
    date = models.DateTimeField('Date', auto_now_add=True)
    from_account = models.ForeignKey(Account, related_name='transaction_from')
    to_account = models.ForeignKey(Account, related_name='transaction_to')

    def __unicode__(self):
        return ("Transfered $%s from %s to %s"
                % (self.amount, self.from_account, self.to_account))
