import os
import fnmatch
import sysconfig

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py

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


class build_py(_build_py):
    def find_package_modules(self, package, package_dir):
        ext_suffix = sysconfig.get_config_vars('EXT_SUFFIX')
        if isinstance(ext_suffix, list):
            ext_suffix = ext_suffix[0]

        modules = super().find_package_modules(package, package_dir)

        filtered_modules = []
        for pkg,mod,filepath in modules:
            if not os.path.exists(filepath.replace('.py', ext_suffix)):
                filtered_modules.append((pkg,mod,filepath))

        print('Filtered Modules:', filtered_modules)
        return filtered_modules

print('Find Packages:', find_packages())
print('Files to Cythonize:', ExtraPaths('abhi'))

setup(
    name='abhi',
    version='0.1.0',
    packages=find_packages(),
    ext_modules = cythonize(
        ExtraPaths('abhi'),
        compiler_directives={'language_level': 3}
    ),
    cmdclass={'build_py': build_py}
)

'''
python setup.py sdist
tar -xvf

Now becomes

python setup.py build_ext --inplace

Then

rm -r build
python setup.py bdist_wheel
'''
