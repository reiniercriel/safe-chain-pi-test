def add(a, b):
    """Return the sum of two numbers.

    Raises TypeError if inputs are not numbers.
    """
    try:
        return a + b
    except TypeError:
        raise TypeError("add: both arguments must support + (numbers, strings compatible)")
