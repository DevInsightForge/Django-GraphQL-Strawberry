from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser


class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "email",
            "password1",
            "password2",
        )
