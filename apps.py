import os
from django.apps import AppConfig


class ExtendedShellConfig(AppConfig):
    name = 'extended_shell'

    def ready(self):
        os.environ.setdefault(
            'PYTHONSTARTUP',
            '{}/startup.py'.format(
                self.path,
            )
        )
