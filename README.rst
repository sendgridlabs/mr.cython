.. contents:: :depth: 1

mr.cython
=========

Problem
-------

Buildout and mr.developer play nice together, until Cython join the party.
There are no unified way to detect/use Cython, some of them (``gevent``) just
use ``cython`` command from ``PATH`` or from ``CYTHON`` environment variable,
others just try to import ``Cython`` modules directly from ``setup.py``.

Solution
--------

Add ``mr.cython`` to the ``extensions`` entry in your ``[buildout]``
section::

  [buildout]
  extensions = mr.cython

If you use ``mr.developer``, add ``mr.cython`` right after them::

  [buildout]
  extensions =
      mr.developer
      mr.cython

This implicitly install ``cython`` into your ``bin/`` directory, and allow 
``setup.py`` from subsequent developed packages find ``cython`` in path, and
allow import ``Cython.*`` namespace from them. Only eggs from ``develop``
line of ``[buildout]`` are affected, including eggs pulled by ``mr.developer``.
