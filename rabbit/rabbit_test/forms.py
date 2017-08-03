from django import forms


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=50)
    file = forms.FileField()


class AuthForm(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput())
