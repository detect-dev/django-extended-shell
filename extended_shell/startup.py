from importlib import import_module

from django.apps import apps
from django.conf import settings  # noqa
from django.core.cache import cache  # noqa
from django.db.models import Avg, Count, F, Max, Min, Q, Sum  # noqa
from django.urls import reverse  # noqa
from django.utils import timezone  # noqa

extra_imports = getattr(
    settings, 'EXTENDED_SHELL_IMPORTS', []
)

for path in extra_imports:
    module_path = key = path

    try:
        module_path, key = path.rsplit('.', 1)
    except ValueError:
        pass

    try:
        module = import_module(module_path)
    except ModuleNotFoundError:
        module = import_module(path)

    locals()[key] = getattr(
        module, key, module)


for model in apps.get_models():
    locals()[model.__name__] = model
