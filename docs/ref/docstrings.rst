.. _ref-docstrings:

Docstrings
==========


Functions and Methods
---------------------
For private methods and functions, please add just a sentence or two stating
what it does. If the functon or method has more than two parameters, you should 
probably document it like you would a public method, but use your good
judgement.

For private, one line functions or methods, you only need a docstring if it's
not immediately obvious what you're doing.

Please document public methods and attributes (methods and attributes that
don't start with an underscore) in the following format.

.. code-block:: python

    def power(num, x):
        """
        This function raises num to the power of x and returns the result

        :type num: int
        :param num: The number to raise

        :type x: int
        :param x: The power to raise the number to

        :rtype: int
        :returns: The result

        :raises: ValueError if x isn't an int

        .. code-block:: python

            >>> result = power(2, 3)
            >>> print result
            8

        """

The rendered output looks like this.

.. autoclass:: my_module
.. autofunction:: my_module.power


Classes
-------
Class documentation can be pretty simple, a sentence or two will usually do.

.. code-block:: python

    class Resource(object):
        """
        A base class for making API calls
        """
        def __init__(self, *args, **kwargs):
            pass


The rendered output looks like this.

.. autofunction:: my_module.Resource

    .. automethod:: __init__

