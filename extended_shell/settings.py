from django.conf import settings

# Enable / Disable colors
EXTENDED_SHELL_COLORED = getattr(
    settings, 'EXTENDED_SHELL_COLORED', True)

# Import models from INSTALLED_APPS
EXTENDED_SHELL_IMPORT_APPS_MODELS = getattr(
    settings, 'EXTENDED_SHELL_IMPORT_APPS_MODELS', True
)

# Custom imports
EXTENDED_SHELL_IMPORTS = getattr(
    settings, 'EXTENDED_SHELL_IMPORTS', [])

# Import usefull utils
EXTENDED_SHELL_DEFAULTS = getattr(
    settings, 'EXTENDED_SHELL_DEFAULTS', [
        'django.conf.settings',
        'django.core.cache.cache',
        'django.utils.timezone',
        'django.db.models.Avg',
        'django.db.models.Count',
        'django.db.models.F',
        'django.db.models.Q',
        'django.db.models.Max',
        'django.db.models.Min',
        'django.db.models.Sum',
    ]
)
