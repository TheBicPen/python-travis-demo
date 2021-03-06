"""
Sample Python project to demonstrate use of Travis-CI

"""

def power_of(base: int, num: int) -> bool:
    """
    Returns True if num is an integer exponent of base, and False otherwise
    """
    value = 1
    for _ in range(num):
        value *= base
        if value == num:
            return True
    return False
