from pyexpat import model
from django import forms
from . import models

from django.contrib.auth.models import User



class UserModelForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class PostModelForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = '__all__'

        












class UserProfileModelForm(forms.ModelForm):

    class Meta():
        model = models.UserProfileModel
        fields = '__all__'





























def chk_fname(value):
    if value != value.capitalize():
        raise forms.ValidationError("Enter Fname in Capitalize Format")



class RegisterForm(forms.Form):


    fname = forms.CharField(max_length=20, validators=[chk_fname])
    lname = forms.CharField(max_length=20)
    email = forms.EmailField()
    prof_link = forms.URLField()
    password = forms.IntegerField()   


    # def clean_fname(self, *args, **kwargs):

    #     f_name = self.cleaned_data.get('fname')

    #     print('##############################################', f_name)

    #     if f_name != f_name.capitalize():

    #         raise forms.ValidationError("Name needs to be in Capitalize format")

    #     return f_name

    # def clean(self, *args, **kwargs):

    #     cleaned_data = self.cleaned_data

    #     fname = cleaned_data['fname']

    #     lname = cleaned_data['lname']

    #     if fname != fname.capitalize() or lname != lname.capitalize():

    #         raise forms.ValidationError("FName and LName needs to be in Capitalize format")
        
    #     return cleaned_data


  
