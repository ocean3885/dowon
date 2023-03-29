from django.forms import ModelForm
from .models import Manseryuk

class ManseryukForm(ModelForm):
    class Meta:
        model = Manseryuk
        fields = '__all__'