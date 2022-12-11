from django import forms
from django import forms
from .models import Resume
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


GENDER_CHOICES = (
 ('Male', 'Male'),
 ('Female', 'Female')
)

CITY_CHOICES = (
 ('Delhi', 'Delhi'),
 ('Mumbai', 'Mumbai'),
 ('Pune', 'Pune'),
 ('Kolkata', 'Kolkata'),
 ('Banglore', 'Banglore'),
 ('Chennai', 'Channai'),
 ('Hydrabad', 'Hydrabad'),
 ('Noida', 'Noida'),
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=CITY_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
        labels = {'name':'Full Name','dob':'Date of birth','pin':'Pin Code','mobile':'Mobile No.','email':'Email Id','job_city':'Job City','profile_image':'Profile Image','my_file':'My File'}
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'pin':forms.NumberInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-select'}),
        'mobile':forms.NumberInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class SignUpForm(UserCreationForm):
    #email = forms.EmailField(max_length=200, help_text='Required', widget=forms.EmailInput(attrs={'placeholder': 'enter your email'})) 
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'enter your password'}))
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'placeholder': 'confirm your password'}))   
    class Meta:
        model = User
        fields = ['username','email']
        widgets = {
            'username':forms.TextInput(attrs={'placeholder': 'enter your username'}),
            'email':forms.EmailInput(attrs={'placeholder': 'enter your email'}),
        }