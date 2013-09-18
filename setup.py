#! /usr/bin/env python
'''
Brian2 setup script
'''
import sys
import os
import warnings

# This will automatically download setuptools if it is not already installed
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
from setuptools.command.install import install as _install


def generate_preferences(dir):
    '''
    Generate a file in the brian2 installation dictionary containing all the
    preferences with their default values and documentation. This file can be
    used as a starting point for setting user- or project-specific preferences.
    '''
    sys.path.insert(0, dir)
    from brian2.core.preferences import brian_prefs
    # We generate the file directly in the install directory
    try:
        with open(os.path.join(dir,
                               'brian2', 'default_preferences'), 'wt') as f:
            defaults = brian_prefs.defaults_as_file
            f.write(defaults)
    except IOError as ex:
        warnings.warn(('Could not write the default preferences to a '
                       'file: %s' % str(ex)))


class install(_install):
    def run(self):
        # Make sure we first run the build (including running 2to3 for Python3)
        # and then import from the build directory
        _install.run(self)

        self.execute(generate_preferences, (self.install_lib, ),
                     msg='Generating default preferences file')


setup(name='Brian2',
      version='2.0dev',
      packages=find_packages(),
      # include template files
      package_data={'': ['*.py_', '*.cpp', '.h']},
      requires=['numpy(>=1.4.1)',
                'scipy(>=0.7.0)',
                'sympy(>=0.7.1)',
                'pyparsing',
                'jinja2(>=2.7)'
                ],
      cmdclass={'install': install},
      use_2to3=True
      )
