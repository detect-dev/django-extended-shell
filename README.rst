
===================
django-extended-shell
===================

.. image:: https://badge.fury.io/py/django-extended-shell.svg
    :target: https://badge.fury.io/py/django-extended-shell.svg

Tiny application that import models from INSTALLED_APPS when `manage.py shell` command is called.


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
