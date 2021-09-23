import os

from setuptools import setup, find_packages

print('Find Packages:', find_packages())
setup(
    name='app',
    version='0.1.0',
    packages=find_packages()
)

# python setup.py sdist
# tar -xvf
