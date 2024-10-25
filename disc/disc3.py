def swipe(n):
    """Print the digits of n, one per line, first backward then forward.

    >>> swipe(2837)
    7
    3
    8
    2
    8
    3
    7
    """
    if n < 10:
        print(n)
        "*** YOUR CODE HERE ***"
    else:
        last_digit = n % 10
        print(last_digit)
        swipe(n // 10)
        print(last_digit)
        
def skip_factorial(n):
    """Return the product of positive integers n * (n - 2) * (n - 4) * ...
    >>> skip_factorial(5) # 5 * 3 * 1

    15
    >>> skip_factorial(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:    #improve: if n <= 2: return n
        return 2
    elif n == 1:    
        return 1
    else:
        return n * skip_factorial(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"    
    def f(i):
        if n % i == 0:
            return False             
        elif n % i != 0:
            return True
        else:
            return f(i + 1)     
    return f(2)


def hailstone(n):
    """Print out the hailstone sequence starting at n, 
    and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    print(n)
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1+ hailstone(n // 2)

def odd(n):
    if n == 1:
        return 1
    return 1 + hailstone(n * 3 + 1)
   

