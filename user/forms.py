from django_registration.forms import RegistrationForm

from .models import MyUser


class MyUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = MyUser
