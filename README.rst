===========
fastinverse
===========

fastinverse_ is a small python extension for optimized interpolation of
data series for which each time point has up to N-th order derivative.

It provides a c:a 5 orders of magnitude faster (albeit less general)
version of `scipy.interpolate.PiecewisePolynomial` (on my dual core laptop I get speed-up of 160 000x). 

See examples/perf.py for a quick head-on benchmark between those two
(expect a runtime on the order of half a minute).  The performance is
achieved through the use of multithreaded (OpenMP) C
 (with some equations generated through Sympy) and Cython.

Feel free to enhance modify and make pull request at `github`__ to

.. _fastinverse: https://github.com/bjodah/fastinverse

__ fastinverse_

Capabilities
============
Fastinverse currently only generates one kind of solver `invnewton` which is 
based on table lookup + newton iteration refinement.

invnewton
---------
InvNewton still has bugs (try changing to -0.7 and it works): 
``` python -m pudb invnewton_main.py -y 'tan(x)' -l 5 -o 3 --sample-N 1000 --x-lo -0.8 --x-hi 1.0 ```


Installation
============
To install run `python setup.py install`.
See distutils' documentation_ for more options.

.. _documentation: http://docs.python.org/2/library/distutils.html

Tests
=====
TODO: make a proper test suite.


Dependencies
============
Python_
NumPy_
Sympy_ 
argh_ (optional, used for command line arguments in example)
Cython_ 0.19 (optional)
pycompilation_ (optional: enables use from python)

.. _Python: http://www.python.org
.. _NumPy: http://www.numpy.org/
.. _Mako: http://www.makotemplates.org/
.. _Cython: http://www.cython.org/
.. _Sympy: http://sympy.org/
.. _pycompilation: https://github.com/bjodah/pycompilation
.. _argh: https://pypi.python.org/pypi/argh

License
=======
Open Soucrce. Released under the very permissive "simplified
(2-clause) BSD license". See LICENCE.txt for further details.

Author
======
Björn Dahlgren, contact (gmail adress): bjodah
