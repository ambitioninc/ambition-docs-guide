Contributing
============

Contributions and issues are most welcome! All issues and pull requests are
handled through github on the `ambitioninc repository`_. Please check for any
existing issues before filing a new one!

.. _ambitioninc repository: https://github.com/ambitioninc/ambition-docs-guide


Documentation Style
-------------------

Please wrap text at 80 characters with a 120 character max.


Building the docs
-----------------

When in the project directory::

    $ pip install -r requirements.txt
    $ cd docs && make html
    $ open docs/_build/html/index.html

Release Checklist
-----------------

Before a new release, please go through the following checklist:

* Bump version in version.py
* Git tag the version
* Add a release note in docs/release_notes/
* Add a link to the newest release note to docs/release_notes/index.rst
