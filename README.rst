*IMPORTANT: ALPHA STATUS, KNOWN BUGS STILL PRESENT (READ BELOW)*

===========
fastinverse
===========

fastinverse_ is a small python extension for generating code which computes
the inverse of a function (which presumably lacks an explicit inverse).

It generates fast C (C99) code for use either tranparently from Python,
or for use in external projects. 

For calculation of large number of inverse values parallelization through OpenMP is used.

Feel free to enhance modify and make pull request at `github`__ to

.. _fastinverse: https://github.com/bjodah/fastinverse

__ fastinverse_


Installation
============
E.g. do:

`pip install --user --upgrade -r http://raw.github.com/bjodah/fastinverse/master/requirements.txt`
`pip install --user --upgrade http://github.com/bjodah/fastinverse/archive/v0.0.3.tar.gz`

(modify to your needs)


Capabilities
============
Fastinverse currently only generates one kind of solver: ``invnewton`` which is 
based on table lookup + newton iteration refinement.

invnewton
---------
InvNewton still has bugs (try changing to -0.8 to -0.7 and it works): 

`python invnewton_main.py -y 'tan(x)' -l 5 -o 3 --sample-N 1000 --x-lo -0.8 --x-hi 1.0`


Installation
============
To install run `python setup.py install`.
See distutils' documentation_ for more options.

.. _documentation: http://docs.python.org/2/library/distutils.html

Using pip it can be installed as:
`pip install --user https://github.com/bjodah/fastinverse/archive/v0.0.2.tar.gz`

Tests
=====
Run `py.test` in root.


Dependencies
============
* Python_
* NumPy_
* Sympy_ 
* argh_ (optional, used for command line arguments in example)
* Cython_ 0.19 (optional)
* pycompilation_ (optional: enables use from python)

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
