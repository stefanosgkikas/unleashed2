from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import the User model
from .models import Profile
from django.utils.text import slugify  # Import slugify function


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    degree = forms.CharField()

    def save(self, commit=True):
        # Save the user account
        user = super().save(commit=commit)
        Profile.objects.update_or_create(user=user, defaults={'slug': slugify(user.get_username())})    
        # Call save_m2m() to save ManyToMany relationships (if any)
        if commit:
            self.save_m2m()
        return user
    
    def clean_username(self):
        username = self.cleaned_data['username']
        disallowed = ('activate', 'create', 'disable', 'login', 'logout', 'password', 'profile')
        if username in disallowed:
            raise ValidationError("A user with that username already exists.")
        return username

    class Meta:
        model = User 
        fields = ('username', 'email', 'age', 'degree', 'password1', 'password2')





