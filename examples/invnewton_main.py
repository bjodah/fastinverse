#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import, unicode_literals

import logging
import os
import time
import sys

import argh
import numpy as np
import sympy
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations,
    implicit_multiplication_application
)


from fastinverse import InvNewtonCode
from fastinverse.core import lambdify


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__file__)

# y=x/(1+x) has the inverse x = y/(1-y)
# for x>-1 and x<-1 (inc/inc)
def main(yexprstr='x/(1+x)', lookup_N = 5, order=3, x_lo=0.0, x_hi=1.0,
         x='x', save_temp=True, sample_N=10240000, check_monotonicity=False,
         itermax=20, nth=102400, silent=False):
    # Parse yexprstr
    yexpr = parse_expr(yexprstr, transformations=(
        standard_transformations + (implicit_multiplication_application,)))
    x = sympy.Symbol(x, real=True)
    yexpr = yexpr.subs({sympy.Symbol('x'): x})

    y = sympy.Symbol('y', real=True)
    explicit_inverse = sympy.solve(yexpr-y,x)
    if explicit_inverse:
        if len(explicit_inverse) == 1:
            print('Explicit inverse: ' + str(explicit_inverse))
            explicit_inverse = explicit_inverse[0]
        else:
            print('No explicit inverse')
            explicit_inverse = None

    # Generate code
    try:
        code = InvNewtonCode(
            yexpr, lookup_N, order, (x_lo, x_hi), x, check_monotonicity,
            save_temp=save_temp, logger=logger, tempdir=os.path.join(
                os.path.dirname(__file__), 'build_invnewton'),)
    except IOError:
        print("Have you run `setup.py build_ext`?")
        raise
    ylim = code.ylim
    mod = code.compile_and_import_binary()

    # Calculate inverse for some randomly sampled values of y on span
    yspan = ylim[1]-ylim[0]
    yarr = ylim[0]+np.random.random(sample_N)*yspan
    t0 = time.time()
    xarr = mod.invnewton(yarr, itermax=itermax)
    trun = time.time()-t0
    print("Runtime (interpolation): ", trun)

    if explicit_inverse:
        cb_expl = lambdify(y, explicit_inverse)
        xarr_expl = cb_expl(yarr).flatten()

    if not silent:
        # Plot the results
        import matplotlib.pyplot as plt

        if explicit_inverse:
            plt.subplot(212)
            plt.plot(yarr[::nth], xarr_expl[::nth]-xarr[::nth], 'x', label='Error')
            plt.ylabel('x')
            plt.xlabel('y')
            plt.legend()
            plt.subplot(211)
            plt.plot(yarr[::nth], xarr_expl[::nth], 'x', label='Analytic')

        plt.plot(yarr[::nth], xarr[::nth], 'o', label='Numerical')
        plt.ylabel('x')
        plt.xlabel('y')
        plt.legend()
        plt.show()

    if explicit_inverse:
        assert np.allclose(xarr_expl, xarr) # our test

argh.dispatch_command(main)
