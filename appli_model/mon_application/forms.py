from django import forms
from .models import ExempleModel

class ExempleModelForm(forms.ModelForm):
    class Meta:
        model = ExempleModel
        fields = '__all__'
