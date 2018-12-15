

def power_of(base: int, num: int) -> bool:
    """
    returns whether num is an integer exponent of base or not
    """
    value = 1
    for i in range(num):
        value *= base
        if value == num:
            return True
    return False
