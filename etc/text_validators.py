from django.core.validators import RegexValidator

COMMENT_PATTERN = RegexValidator(
    regex=r'^.{20,1000}$',
    message='comment should be at least 20 characters and at most 1000 characters',
    code='invalid_comment'
)
