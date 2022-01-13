from django import forms
from contact_us.models import Contact_Us


class contact_us_Form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "contact_input contact_input_name inpt", 'placeholder': " Name", 'name': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "contact_input contact_input_name inpt", 'placeholder': "Email", 'name': 'email'}))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={"class": "contact_input contact_input_name inpt", 'placeholder': " subject", 'name': 'subject'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "contact_textarea contact_input inpt", 'placeholder': "message", 'name': 'message'}))

    class Meta:
        model = Contact_Us
        fields = ['name', 'email', 'subject', 'message', ]
