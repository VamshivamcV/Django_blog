from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": (
                    "w-full px-4 py-2 rounded-lg "
                    "border border-gray-300 "
                    "focus:ring-2 focus:ring-green-500 "
                    "focus:border-green-500 outline-none"
                )
            })

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class TailwindLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                "class": (
                    "w-full px-4 py-2 rounded-lg "
                    "border border-green-300 "
                    "focus:ring-2 focus:ring-green-500 "
                    "focus:border-green-500 outline-none"
                )
            })
