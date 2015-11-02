# -*- coding: utf-8 -*-

import glob
import os
import subprocess
import sys

def run_example(pypath):
    p = subprocess.Popen(
        ['python3' if sys.version_info.major == 3 else 'python',
         pypath, '--silent'],
        cwd=os.path.join(os.path.dirname(__file__),'..'))
    assert p.wait() == 0 # systems which have `make` have SUCCESS==0

def test_invnewton():
    run_example(os.path.join(
        os.path.dirname(__file__), '..', 'invnewton_main.py'))
