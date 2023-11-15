from django.core.validators import RegexValidator
from django.db import models

rating_validator = RegexValidator(
    regex=r'^[1-5]$',
    message='Rating must be between 1 and 5.',
)
