from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        #del self.fields['username']
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['handle'].widget.attrs.update({'class' : 'form-control'})
        self.fields['about_me'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password1'].widget.attrs.update({'class' : 'form-control'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control'})
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'handle', 'about_me', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        #del self.fields['username']
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})

    class Meta:
        model = Account
        fields = ('email',)