import os

from setuptools import setup, find_packages
from Cython.Build import cythonize


EXCLUDE_FILES = ['abhi/extra.py']


def ExtraPaths(root_dir):
    paths = []
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if os.path.splitext(filename)[1] == '.py':
                filepath = os.path.join(root, filename)
                
                if filepath not in EXCLUDE_FILES:
                    paths.append(filepath)
    return paths

print('Find Packages:', find_packages())
print('Files to Cythonize:', ExtraPaths('abhi'))

setup(
    name='abhi',
    version='0.1.0',
    packages=find_packages(),
    ext_modules = cythonize(
        ExtraPaths('abhi'),
        compiler_directives={'language_level': 3}
    )
)

'''
python setup.py sdist
tar -xvf

Now becomes

python setup.py build_ext --inplace
'''
