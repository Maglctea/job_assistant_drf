from django import forms
from landingapp.models import User


class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'