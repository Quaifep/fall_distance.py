# Author: Paul Quaife
# Date: 1/27/2021
# Description: Function returns the distance in meters that the object has fallen in that time.

def fall_distance(falling_time):
    """Returns the distance in meters that object has fallen in time."""
    return 0.5 * 9.8 * falling_time * falling_time
