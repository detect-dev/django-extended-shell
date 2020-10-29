import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-extended-shell",
    version="0.1.4",
    author="Dmitry Bobrovitsky",
    author_email="detect.dev@gmail.com",
    description="Django shell with imported models",
    long_description=long_description,
    url="https://github.com/detect-dev/django-extended-shell",
    packages=['extended_shell'],
    classifiers=[
        'Framework :: Django',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
