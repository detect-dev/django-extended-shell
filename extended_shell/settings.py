from django.conf import settings

# Enabled/Disabled colors
EXTENDED_SHELL_COLORED = getattr(
    settings, 'EXTENDED_SHELL_COLORED', True)

# Import models from INSTALLED_APPS
EXTENDED_SHELL_IMPORT_APPS_MODELS = getattr(
    settings, 'EXTENDED_SHELL_IMPORT_APPS_MODELS', True
)

# Import usefull utils, such as timezone, cache etc.
EXTENDED_SHELL_IMPORT_DEFAULTS = getattr(
    settings, 'EXTENDED_SHELL_IMPORT_DEFAULTS', True
)

# Custom imports
EXTENDED_SHELL_IMPORTS = getattr(
    settings, 'EXTENDED_SHELL_IMPORTS', [])
