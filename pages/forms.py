from django.forms import ModelForm
from django import forms
from .models import Contact

# Contact Form
class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields = '__all__'
        
