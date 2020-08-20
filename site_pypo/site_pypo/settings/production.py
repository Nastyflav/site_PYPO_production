from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


sentry_sdk.init(
    dsn="https://6a3c0b450f574bbc8835ef6c51941301@o401185.ingest.sentry.io/5398165",
    integrations=[DjangoIntegration()],

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
