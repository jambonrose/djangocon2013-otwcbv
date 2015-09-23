# bank/forms.py
from django.forms import ModelForm
from django.forms.widgets import HiddenInput
from django.utils.text import slugify
from .models import Account, Transaction

class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ('slug',)
    
    def save(self, commit=True):
        instance = super(AccountForm, self).save(commit=False)
        instance.slug = slugify(self.cleaned_data.get('name', ''))
        if commit:
            instance.save()
            self.save_m2m()
        return instance

class TransferFormFrom(ModelForm):
    class Meta:
        model = Transaction
        fields= '__all__'
        widgets = {
            'from_account': HiddenInput(),
        }

class TransferFormTo(ModelForm):
    class Meta:
        model = Transaction
        fields= '__all__'
        widgets = {
            'to_account': HiddenInput(),
        }
