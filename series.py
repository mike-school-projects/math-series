def fibonacci(n):
    """
    Returns the nth sequence Fibonacci number

    :return:
    Fn = Fn-1 + Fn-2
    """

    # base case (end case)
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    Returns the nth sequence Lucas number
    Similar to Fibonacci, but with different starting points

    :return:
    Fn = Fn-1 + Fn-2
    """

    # base case (end case)
    if n <= 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, num0=0, num1=1):
    """
    Returns the nth sequence of a fibonacci-like series using optional different starting points

    :return:
    Fn = Fn-1 + Fn-2
    """

    # base case (end case)
    if n <= 0:
        return num0
    if n == 1:
        return num1
    return sum_series(n-1, num0, num1) + sum_series(n-2, num0, num1)


