.. _ref-docstrings:

Docstrings
==========


Functions and Methods
---------------------
Please document functions and methods in the following format.

.. code-block:: python

    def pow(num, x):
        """
        This function raises num to the power of x and returns the result

        :type num: int
        :param num: The number to raise

        :type x: int
        :param x: The power to raise the number to

        :rtype: int
        :returns: The result

        .. code-block:: python

            >>> result = pow(2, 3)
            >>> print result
            8

        """

Classes
-------
Class documentation can be pretty simple.

.. code-block:: python

    class Resource(object):
        """
        A base class for making API calls
        """
        def __init__(self, *args, **kwargs):
            pass
