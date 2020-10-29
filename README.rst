
======================
django-extended-shell
======================

.. image:: https://badge.fury.io/py/django-extended-shell.svg
    :target: https://badge.fury.io/py/django-extended-shell

A tiny application that import models from INSTALLED_APPS when `manage.py shell` command called.


Getting It
==========
You can get django-extended-shell by using pip::

    $ pip install django-extended-shell


Installing It
=============

To enable `django-extended-shell` in your project you need to add it to `INSTALLED_APPS` in your projects
`settings.py` file::

    INSTALLED_APPS = (
        ...
        'extended_shell',
        ...
    )


Settings
=============

Available settings, see extended_shell/settings.py
::
  
    # Enable or disable import colors (Default: True)
    EXTENDED_SHELL_COLORED = True

    # Import models from INSTALLED_APPS (Default: True)
    EXTENDED_SHELL_IMPORT_APPS_MODELS = True

    # List of custom user modules
    EXTENDED_SHELL_IMPORTS = []

    # List of usefull django utils
    EXTENDED_SHELL_DEFAULTS = [
        'django.conf.settings',
        'django.core.cache.cache',
        'django.utils.timezone',
        'django.db.models.Avg',
        'django.db.models.Count',
        'django.db.models.F',
        'django.db.models.Q',
        'django.db.models.Max',
        'django.db.models.Min',
        'django.db.models.Sum'
    ]