# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import, unicode_literals


from fastinverse import InvNewtonCode
from fastinverse.core import lambdify

import numpy as np
import sympy

RANDOM_SEED = 42

def test_InvNewtonCode():
    x, y = sympy.symbols('x y')
    expr1 = x/(1+x)
    expl_inv = sympy.solve(sympy.Eq(y,expr1), x)
    lookup_N, order, xlim = 10, 1, (0,1)
    invnewton = InvNewtonCode(expr1, lookup_N, order, xlim, x, True)
    ylim = invnewton.ylim
    mod = invnewton.compile_and_import_binary()

    yspan = ylim[1]-ylim[0]
    np.random.seed(RANDOM_SEED)
    yarr = ylim[0]+np.random.random(100)*yspan
    xarr = mod.invnewton(yarr, itermax=100)

    cb_expl = lambdify(y, expl_inv)
    xarr_expl = cb_expl(yarr).flatten()

    assert np.allclose(xarr, xarr_expl)
    invnewton.clean()

if __name__ == '__main__':
    test_InvNewtonCode()
