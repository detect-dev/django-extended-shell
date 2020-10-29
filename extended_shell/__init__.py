from importlib import import_module

default_app_config = 'extended_shell.apps.ExtendedShellConfig'


def extra_import(pathes):
    values = {}

    for path in pathes:
        module_path = key = path

        try:
            module_path, key = path.rsplit('.', 1)
        except ValueError:
            pass

        try:
            module = import_module(module_path)
        except ModuleNotFoundError:
            module = import_module(path)

        values[key] = getattr(
            module, key, module)

    return values
