from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from app.models import Profile


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password',
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)
        help_texts = {
            'username': None,
            'email': None,
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar',)


UserProfileInlineFormset = inlineformset_factory(
    User,
    Profile,
    form=UpdateProfileForm,
    can_delete=False,
)
