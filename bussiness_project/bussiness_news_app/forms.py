from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Posts, AboutAuthor
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserForm(UserCreationForm):# forms.ModelForm):
    first_name = forms.CharField(max_length=30, help_text='Optional.')
    last_name = forms.CharField(max_length=30, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class AccountAuthenticationForm(forms.ModelForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['email', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")


class PostForm(forms.ModelForm):

    author = forms.CharField(max_length=35)
    article = forms.CharField(widget=forms.Textarea)
    title = forms.CharField(max_length=50)
    image = forms.FileField()
    article_permission = forms.CharField(max_length=35)

    class Meta:
        model = Posts
        fields = ['author', 'title', 'article', 'image', 'article_permission']


class AboutAuthorForm(forms.ModelForm):

    author = forms.CharField(max_length=35)
    description = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
    fullname = forms.CharField(max_length=40)

    class Meta:
        model = AboutAuthor
        fields = ['author', 'description', 'image', 'fullname']
