from django.apps import apps
from django.conf import settings # noqa
from django.core.cache import cache  # noqa
from django.db.models import Avg, Count, F, Max, Min, Q, Sum  # noqa
from django.urls import reverse  # noqa
from django.utils import timezone  # noqa

from extended_shell import extra_import
from extended_shell import settings as conf


locals().update(
    extra_import(conf.EXTENDED_SHELL_IMPORTS)
)

locals().update({
    model.__name__: model for
    model in apps.get_models()
})


del extra_import
del conf, apps
