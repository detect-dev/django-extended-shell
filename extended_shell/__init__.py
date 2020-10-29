
import sys
from importlib import import_module
from django.core.management.base import OutputWrapper
from django.core.management.color import color_style
from . import settings

default_app_config = 'extended_shell.apps.ExtendedShellConfig'

style = color_style(
    settings.EXTENDED_SHELL_COLORED
)

term = OutputWrapper(
    sys.stdout
)


def show_modules(modules):
    imports = {}

    for module in modules:
        if isinstance(module, str):
            try:
                module, name = module.rsplit('.', 1)
            except ValueError:
                name = None
        else:
            try:
                name = module.__name__
                module = module.__module__
            except Exception:
                continue

        imports.setdefault(
            module, [])

        if name is not None:
            imports[module].append(name)

    relative, fixed = [], []

    for module, names in imports.items():
        names = ', '.join(names)

        if names:
            relative.append('from {} import {}'.format(
                module, names))
        else:
            fixed.append('import {}'.format(
                module))

    for line in fixed + relative:
        term.write(style.SUCCESS(line))


def load_modules(pathes):
    imports = {}

    for path in pathes:
        module_path = key = path

        try:
            module_path, key = path.rsplit('.', 1)
        except ValueError:
            pass

        module = import_module(
            module_path)

        imports[key] = getattr(
            module, key, module)

    return imports
