
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
    if type(x) != int:
        raise ValueError('x must be an int')
    return pow(num, x)


class Resource(object):
    """
    A base class for making API calls
    """
    def __init__(self, *args, **kwargs):
        pass

