
from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('owner','status','created','updated','Mpesa_transid','paid','discount',)

        def clean_phone(self):
            phone = self.cleaned_data['phone']
            if len(phone) < 10:
                raise forms.ValidationError('Enter a valid phone number.(e.g.07********)')
            return self.cleaned_data['phone']


