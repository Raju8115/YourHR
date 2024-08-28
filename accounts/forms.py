from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    usable_password = None
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input'})
        self.fields['email'].widget.attrs.update({'class': 'form-input'})
        self.fields['password1'].widget.attrs.update({'class': 'form-input'})
        self.fields['password2'].widget.attrs.update({'class': 'form-input'})
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None  # Removes default help texts

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")

        # Check for other constraints here
        return cleaned_data

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['resume']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Adding Tailwind CSS classes to the file input field
            self.fields['resume'].widget.attrs.update({'class': 'form-input'})
