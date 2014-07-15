.. _ref-autodoc:

Autodoc
=======
See the `Sphinx autodoc`_ page for full documentation.

.. _Sphinx autodoc: http://sphinx-doc.org/ext/autodoc.html#module-sphinx.ext.autodoc

Functions
---------
To document the function ``mymodule.power``::

    .. autofunction:: mymodule.power

Classes
-------
To automatically document classes::

    .. autoclass:: my_module.MyClass
        :members:
        :undoc-members:

* The ``:members:`` option will automatically generate all documented methods
* The ``:undoc-members:`` option will document all undocumented methods
* The ``:private-members:`` option will document private options (methods that
    start with one or two underscores. Ex: ``_private``)

Modules
-------
To document your module::

    .. automodule:: mymodule
