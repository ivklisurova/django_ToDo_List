from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
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


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'


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
    # extra=5,
    # max_num=5,
    # fk_name=None,
    # fields=None, exclude=None, can_order=False,
    # can_delete=True, max_num=None, formfield_callback=None,
    # widgets=None, validate_max=False, localized_fields=None,
    # labels=None, help_texts=None, error_messages=None,
    # min_num=None, validate_min=False, field_classes=None
)
