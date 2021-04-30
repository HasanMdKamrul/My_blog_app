from django import forms
from marketing.models import Signup

class SigunupModelForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ("email",)