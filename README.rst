
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
Available settings::

    EXTENDED_SHELL_COLORED = False # Disable terminal colors
    EXTENDED_SHELL_IMPORT_APPS_MODELS = False # Disable app models import
    EXTENDED_SHELL_DEFAULTS = [] # Disable default utils import
    EXTENDED_SHELL_IMPORTS = [] # Add custom imports
