
from django.core.exceptions import ValidationError

def only_num(value):
    if len(value) > 5:
        raise ValidationError('너무깁니다')