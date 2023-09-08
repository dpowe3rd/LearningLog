from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')  # Fields associated with 'auth.get_user_model'
        model = get_user_model()

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        self.fields['username'].label = "Display Name"  # Setting a label for the field 'username'
        self.fields['email'].label = "Email Address"  # Setting a label for the field 'email'
