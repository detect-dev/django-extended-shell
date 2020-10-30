
import sys
from collections import namedtuple
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

Import = namedtuple('Import', [
    'module',
    'name',
    'alias'
])


def parse_import(path):
    try:
        path, alias = path.rsplit(' as ', 1)
        alias = alias.strip()
    except ValueError:
        alias = None

    module_path = name = path

    try:
        module_path, name = path.rsplit('.', 1)
    except ValueError:
        pass

    return Import(
        module_path.strip(),
        name.strip(),
        alias
    )


def show_modules(modules):
    imports = {}
    strings = []

    for module in modules:
        if isinstance(module, str):
            data = parse_import(module)
        else:
            try:
                data = Import(
                    module.__module__,
                    module.__name__,
                    None
                )
            except AttributeError:
                continue

        name = (
            data.module or
            repr(data)
        )

        imports.setdefault(name, [])
        imports[name].append(data)

    for module, datas in imports.items():
        tmpl = 'from {path} import {modules}'

        modules = []
        for data in datas:
            if not data.module:
                tmpl = 'import {modules}'

            modules.append(
                '{imp.name} as {imp.alias}'.format(imp=data)
                if data.alias else data.name
            )

        strings.append(
            tmpl.format(
                path=module,
                modules=', '.join(modules)
            ))

    for line in reversed(strings):
        term.write(style.SUCCESS(line))


def load_modules(pathes):
    imports = {}

    for path in pathes:
        data = parse_import(path)

        module = import_module(
            data.module or data.name
        )

        imports[data.alias or data.name] = getattr(
            module,
            data.name,
            module
        )

    return imports
