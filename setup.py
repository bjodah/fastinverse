#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob

from distutils.core import setup
from distutils.command import build

pyx_path = 'fastinverse/invnewton_wrapper.pyx'


class my_build(build.build):
    def run(self):
        build.build.run(self)
        try:
            from pycompilation import pyx2obj
            from pycompilation.util import copy, make_dirs
        except ImportError:
            print("Could not import `pycompilation`, invnewton won't work from python.'")
            return
        if self.dry_run: return# honor the --dry-run flag
        copy(pyx_path, self.build_temp,
             dest_is_dir=True, create_dest_dirs=True)
        prebuilt_temp = os.path.join(
            self.build_temp, 'prebuilt/')
        make_dirs(prebuilt_temp)
        obj_path = pyx2obj(pyx_path, prebuilt_temp,
                           interm_c_dir=prebuilt_temp,
                           metadir=prebuilt_temp,
                           )
        if self.inplace:
            prebuilt_lib = 'fastinverse/prebuilt/'
        else:
            prebuilt_lib = os.path.join(
                self.build_lib, 'fastinverse/prebuilt/')
        make_dirs(prebuilt_lib)
        copy(obj_path, prebuilt_lib)
        copy(glob.glob(prebuilt_temp+'.meta*')[0], prebuilt_lib)


setup(
    name='fastinverse',
    version='0.0.3',
    description='Python package using SymPy for generating fast C code solving inverse problems.',
    author='Björn Dahlgren',
    author_email='bjodah@DELETEMEgmail.com',
    url='https://github.com/bjodah/fastinverse',
    packages=['fastinverse'],
    cmdclass = {'build': my_build},
)
