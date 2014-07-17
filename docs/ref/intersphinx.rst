.. _ref-intersphinx:

Intersphinx
===========
`Intersphinx`_ is a built-in Sphinx module that allows for mapping to other project's documentation. An example would be
that you want to specify that your function accepts a Django model as a parameter.

Setup
-----
The file ``/docs/conf.py`` will have your sphinx configuration and will need the ``intersphinx_mappings`` directive
configured. Ambition's `ambition-python-template`_ and `django-app-template`_ both already have this set up. You will
also need to make sure the library is in ``requirements/docs.txt``.

.. code-block:: python

    intersphinx_mapping = {
        'python': ('http://python.readthedocs.org/en/v2.7.2/', None),
        'django': ('http://django.readthedocs.org/en/latest/', None),
        'celery': ('http://celery.readthedocs.org/en/latest/', None),
    }

.. _Intersphinx: http://sphinx-doc.org/ext/intersphinx.html
.. _django-app-template: https://github.com/ambitioninc/django-app-template
.. _ambition-python-template: https://github.com/ambitioninc/ambition-python-template/

Usage
-----
To use intersphinx in your documentation or docstrings, use the following format:

.. code-block:: python

    def my_function(model):
        """
        :type model: :class:`Models<django:django.db.models.Model>`
        :param model: The model you want work with
        """
        pass


The link will look like this :class:`Models<django:django.db.models.Model>`.
