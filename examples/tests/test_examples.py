# -*- coding: utf-8 -*-

import os
import subprocess
import sys


def run_example(pypath):
    p = subprocess.Popen(
        ['python%d.%d' % (sys.version_info.major, sys.version_info.minor),
         pypath, '--silent'],
        cwd=os.path.join(os.path.dirname(__file__), '..'))
    assert p.wait() == 0  # systems which have `make` have SUCCESS==0


def test_invnewton():
    run_example(os.path.join(
        os.path.dirname(__file__), '..', 'invnewton_main.py'))
