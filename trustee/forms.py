from django import forms
from .models import ContactUs,Contact


class HomeForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ('',)


class ContactForm1(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('',)