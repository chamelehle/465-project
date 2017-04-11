from django import forms
from .models import submit, fact, aboutl
from django.core.validators import validate_slug

def verify_comments(value):
        return value

class SubmitForm(forms.Form):
    user_name = forms.CharField(
        max_length=250,
        label='Name:',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter name'
            }))
    date = forms.CharField(
        max_length=30,
        label='Date:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter date of event'
            }))
    user_input = forms.CharField(
        max_length=500,
        label='Description:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter description'
            }))
class FactForm(forms.Form):
    user_name = forms.CharField(
        max_length=250,
        label='Title:',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter name'
            }))
    date = forms.CharField(
        max_length=30,
        label='URL:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter url source'
            }))
    user_input = forms.CharField(
        max_length=500,
        label='Description:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter description'
            }))
class AboutForm(forms.Form):
    user_name = forms.CharField(
        max_length=250,
        label='Title:',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'enter name'
            }))
    date = forms.CharField(
        max_length=30,
        label='URL:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter url source'
            }))
    user_input = forms.CharField(
        max_length=500,
        label='Description:',
        widget=forms.TextInput(attrs={
            'placeholder': 'enter description'
            }))
