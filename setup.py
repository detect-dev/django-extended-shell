import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-extended-shell",
    version="0.0.3",
    author="Dmitry Bobrovitsky",
    author_email="detect.dev@gmail.com",
    description="Django shell with imported models",
    long_description="A tiny application that import models from INSTALLED_APPS when `manage.py shell` command called.", # noqa
    long_description_content_type="text/markdown",
    url="https://github.com/detect-dev/django-extended-shell",
    packages=['extended_shell'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
