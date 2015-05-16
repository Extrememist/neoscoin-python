neoscoin-python is a set of Python libraries that allows easy access to the
neoscoin peer-to-peer cryptocurrency client API.

Not actively maintained
===========================
neoscoin-python is not actively maintained. I don't have the mental bandwidth
to maintain it and good alternatives have sprung up over time.

I'd suggest python-neoscoinlib (https://github.com/petertodd/python-neoscoinlib )
as is the ultimate python neoscoin library. It offers not only RPC access but
also a Python version of almost every neoscoin data structure.

The RPC is can be used through `neoscoin.rpc.Proxy`, see for example
https://github.com/petertodd/python-neoscoinlib/blob/master/examples/make-bootstrap-rpc.py.

If anyone wants to take up the maintainer role for neoscoin-python, let me know.

Documentation
===========================

Documentation can be found here, or in the source archive. It is built
using Sphinx:

http://extrememist.github.com/neoscoin-python/doc/

Installation instructions
===========================

neoscoin-python uses setuptools for the install script. There are no dependencies apart from Python itself.

::

  $ python setup.py build
  $ python setup.py install

Pypi / Cheeseshop
==================

It is possible to install the package through Pypi (cheeseshop), see http://pypi.python.org/pypi?:action=display&name=neoscoin-python

::

  $ pip install neoscoin-python

TODO
======
These things still have to be added:

- SSL support (including certificate verification) for managing remote neoscoin daemons.

