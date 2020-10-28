from django.apps import apps
from django.conf import settings  # noqa
from django.core.cache import cache  # noqa
from django.db.models import Avg, Count, F, Max, Min, Q, Sum  # noqa
from django.urls import reverse  # noqa
from django.utils import timezone  # noqa

for model in apps.get_models():
    locals()[model.__name__] = model
