#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from distutils.core import setup
from distutils.command import build_ext

pyx_name = 'invnewton_wrapper.pyx'
package_dir = 'fastinverse'
prebuilt_dir = 'prebuilt'

DEBUG=True

class my_build_ext(build_ext.build_ext):
    def run(self):
        if not self.dry_run: # honor the --dry-run flag
            try:
                from pycompilation import pyx2obj
                from pycompilation.util import copy
                obj_path = pyx2obj(pyx_name, prebuilt_dir,
                                   interm_c_dir=prebuilt_dir,
                                   metadir=prebuilt_dir,
                                   cwd=package_dir)
                copy(obj_path, prebuilt_dir)
            except ImportError:
                print("Could not import `pycompilation`, invnewton won't work from python.'")


setup(
    name='fastinverse',
    version='0.0.1',
    description='Python package using SymPy for generating fast C code solving inverse problems.',
    author='Björn Dahlgren',
    author_email='bjodah@DELETEMEgmail.com',
    url='https://github.com/bjodah/fastinverse',
    packages=['fastinverse'],
    cmdclass = {'build_ext': my_build_ext},
)
