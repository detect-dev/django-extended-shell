from django.apps import apps
from extended_shell import settings as conf
from extended_shell import (
    show_modules,
    load_modules,
    term
)


if conf.EXTENDED_SHELL_DEFAULTS:
    term.write('# Extended shell django imports')
    modules = conf.EXTENDED_SHELL_DEFAULTS

    locals().update(
        load_modules(modules))

    show_modules(
        modules
    )


if conf.EXTENDED_SHELL_IMPORT_APPS_MODELS:
    term.write('# Extended shell model imports')
    models = apps.get_models()

    locals().update({
        model.__name__: model for
        model in models
    })

    show_modules(
        models
    )

if conf.EXTENDED_SHELL_IMPORTS:
    term.write('# Extended shell custom imports')
    modules = conf.EXTENDED_SHELL_IMPORTS

    locals().update(
        load_modules(modules))

    show_modules(
        modules
    )

del (
    load_modules,
    show_modules,
    apps,
    conf,
    term
)
