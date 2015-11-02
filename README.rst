===========
fastinverse
===========

.. image:: https://travis-ci.org/bjodah/fastinverse.png?branch=master
   :target: https://travis-ci.org/bjodah/fastinverse

fastinverse_ is a small python extension for generating code which computes
the inverse of a function (which presumably lacks an explicit inverse).

It generates fast C (C99) code for use either tranparently from Python,
or for use in external projects. 

For calculation of large number of inverse values parallelization through OpenMP is used.

Feel free to enhance modify and make pull request at `github`__.

.. _fastinverse: https://github.com/bjodah/fastinverse

__ fastinverse_


Installation
============
E.g.

::

   $ pip install --user --upgrade -r http://raw.github.com/bjodah/fastinverse/master/requirements.txt
   $ pip install --user --upgrade http://github.com/bjodah/fastinverse/archive/v0.0.6.tar.gz


(modify to your needs)


Capabilities
============
Fastinverse currently only generates one kind of solver: ``invnewton`` which is 
based on table lookup of polynomial coefficient + interpolation + newton iteration refinement.

invnewton
---------

``python invnewton_main.py -y 'tan(x)' -l 5 -o 3 --sample-N 1000 --x-lo -0.7 --x-hi 0.7``

Example
-------

.. code:: python

   >>> import sympy
   >>> from fastinverse import InvNewtonCode
   >>> x = sympy.Symbol('x')
   >>> y = x/(1+x)  # inverse: y/(1-y)
   >>> lookup_N, order, xlim = 10, 1, (0,1)
   >>> invnewton = InvNewtonCode(y, lookup_N, order, xlim, x)
   >>> ylim = invnewton.ylim
   >>> mod = invnewton.compile_and_import_binary()
   >>> mod.invnewton(0.4, itermax=100)  # .4/.6
   [ 0.333333333]


Tests
=====
Run ``py.test``


Dependencies
============
* Python_
* NumPy_
* Sympy_ 
* argh_ (optional, used for command line arguments in example)
* Cython_ 0.19 (optional)
* pycompilation_ (optional: enables use from python)
* pycodeexport_ (optional: enables use from python)
* symvarsub_ (optional)
* matplotlib_ (optional)

.. _Python: http://www.python.org
.. _NumPy: http://www.numpy.org/
.. _Mako: http://www.makotemplates.org/
.. _Cython: http://www.cython.org/
.. _Sympy: http://sympy.org/
.. _pycompilation: https://github.com/bjodah/pycompilation
.. _pycodeexport: https://github.com/bjodah/pycodeexport
.. _argh: https://pypi.python.org/pypi/argh
.. _symvarsub: https://github.com/bjodah/symvarsub
.. _matplotlib: http://matplotlib.org

License
=======
Open Source. Released under the very permissive "simplified
(2-clause) BSD license". See LICENCE.txt for further details.

Author
======
Björn Dahlgren, contact (gmail adress): bjodah
