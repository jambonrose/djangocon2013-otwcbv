# bank/forms.py
from django.forms import ModelForm
from django.utils.text import slugify
from .models import Account

class AccountForm(ModelForm):
    class Meta:
        model = Account
    
    def clean(self):
        cleaned_data = super(AccountForm, self).clean()
        name = cleaned_data.get("name")
        slug = cleaned_data.get("slug")
    
        if not slug and name:
            cleaned_data['slug'] = slugify(name)
    
        return cleaned_data
