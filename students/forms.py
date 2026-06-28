from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(UserCreationForm):
    email = forms.EmailField(required=True)
    reg_number = forms.CharField(max_length=50, label="Registration Number", required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'reg_number', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['reg_number']  # use reg number as username
        if commit:
            user.save()
        return user
    
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)#, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    reg_number = forms.CharField(max_length=50, label="Registration Number", widget=forms.TextInput(attrs={'placeholder': 'Reg Number'}))

    class Meta:
        model = User
        fields = ['reg_number', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['reg_number'] # Login with reg number
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            print("User saved:", user.id, user.username)
        return user

    