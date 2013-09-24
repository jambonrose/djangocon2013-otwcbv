# bank/forms.py
from django.forms import ModelForm
from django.utils.text import slugify
from .models import Account

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
