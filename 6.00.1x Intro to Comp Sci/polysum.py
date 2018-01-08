# Evan Douglass

# This program contains a function that sums the area and square of the
# perimiter of a polygon.

import math

def polysum(n, s):
    '''
    n is an int or float that represents the number of sides of a polygon.
    s is an int or a float and represents the length of each side.

    Returns the sum of the area and the square of the perimiter as a float.
    '''
    # find area and squared perimeter
    area = (0.25 * n * s**2) / math.tan(math.pi / n)
    p_sqrd = (n * s)**2

    # sum the values
    p_sum = area + p_sqrd

    return round(p_sum, 4)
