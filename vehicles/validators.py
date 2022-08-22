from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

def validate_future_date(value):
        today = timezone.now()
        if value > today.date():
            raise ValidationError(_('The date cannot be in the future'))

