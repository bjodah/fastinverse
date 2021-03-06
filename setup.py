#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import sys

from distutils.core import setup
from distutils.command import build

version_ = '0.0.7'
name_ = 'fastinverse'

pyx_path = os.path.join(name_, '_invnewton.pyx')


if '--help' in sys.argv[1:] or sys.argv[1] in (
        '--help-commands', 'egg_info', 'clean', '--version'):
    cmdclass_ = {}
    ext_modules_ = []
else:
    from pycodeexport.dist import pce_build_ext
    from pycodeexport.codeexport import make_PCEExtension_for_prebuilding_Code
    from fastinverse.core import InvNewtonCode

    cmdclass_ = {'build_ext': pce_build_ext}
    ext_modules_ = [
        make_PCEExtension_for_prebuilding_Code(
            name_+'._invnewton', InvNewtonCode,
            ['_invnewton.pyx'],
            srcdir=name_,
            logger=True
        ),
    ]


setup(
    name=name_,
    version=version_,
    author='Björn Dahlgren',
    author_email='bjodah@DELETEMEgmail.com',
    description='Python package using SymPy for generating fast C code solving inverse problems.',
    license = "BSD",
    url='https://github.com/bjodah/'+name_,
    download_url='https://github.com/bjodah/'+name_+'/archive/v'+version_+'.tar.gz',
    packages=[name_],
    ext_modules = ext_modules_,
    cmdclass = cmdclass_,
)
