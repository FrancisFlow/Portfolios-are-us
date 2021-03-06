from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Profile, Rating

# Create your forms here 

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model= User
        fields=('username', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user=super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['user', 'post_date']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ['name', 'phone_number', 'profile_pic', 'bio']

class ProjectRateForm(forms.ModelForm):
    class Meta:
        model=Rating
        exclude = ['pub_date', 'user', 'post']

