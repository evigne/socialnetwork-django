from django import forms #to use forms from django
from django.contrib.auth.models import User # to use User model from django
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import UserProfile

class RegistrationForm(UserCreationForm):
     email = forms.EmailField(required=True)

     class Meta:
         model = User
         fields = (
             "username",
             "first_name",
             "last_name",
             "email",
             "password1",
             "password2"
         )

     def save(self, commit=True):
         """
         username ,password1, password2 already inherited from UserCreationForm
         """
         user = super(RegistrationForm, self).save(commit=False)
         user.first_name = self.cleaned_data['first_name']
         user.last_name = self.cleaned_data['last_name']
         user.email = self.cleaned_data['email']

         if commit:
             user.save()

         return user

class ProfileEdit(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (""
                  "description",
                  "city",
                  "website",
                  "phone",
                  "image"
                  )


class EditProfileForm(UserChangeForm):



    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )
        """ 
        or we can use
        exclude = ('list of field we need to exclude')
        """




"""

# User creation form from django docs for reference

class UserCreationForm(forms.ModelForm):
    
    # A form that creates a user, with no privileges, from the given username and
    # password.
    
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("username",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user
"""