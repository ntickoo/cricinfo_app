from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import datetime

def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False

def validate_event_date(date):
    if not validate(date):
        raise ValidationError(
            _('%(date)s is not in valid format of YYYY-MM-DD'),
            params={'value': date},
        )