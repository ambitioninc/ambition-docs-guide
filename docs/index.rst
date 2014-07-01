Ambition Docs Guide Documentation
=================================
This guide is meant for developers new to reStructuredText and Sphinx to
quickly pick up key points for adding documentation to python code and
projects.

Overview
========
`Sphinx`_ is a tool that generates documentation from reStructuredText. Output
formats include HTML, pdf, epub, manpage, and many others.

`reStructuredText`_ is a markup language primarily for python documentation.

.. _Sphinx: http://sphinx-doc.org/
.. _reStructuredText: http://docutils.sourceforge.net/rst.html

Getting Started
===============
In all current Ambition app templates, there is now a ``docs`` folder in the
root of the project, this is the source for Sphinx documentation.

Common reStructuredText and Sphinx commands will be documented here:

* :doc:`Python Docstrings <ref/docstrings>`
* :doc:`Using Sphinx Autodoc <ref/autodoc>`
* `Sphinx reStructuredText primer`_


.. _Sphinx reStructuredText primer: http://sphinx-doc.org/rest.html#rst-primer

Release Notes
=============

.. toctree::

   release_notes/v0.1

Contributing
============

Please see :doc:`Contributing <contributing>`
