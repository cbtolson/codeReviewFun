# Author: Chanin Woods
# Built: python v.3.3
# Updated: 24 February 2017
import pytest
from move_car import *

############################################################################
# Function to test code (command line input)
# Input: x (float position), y (float position), dir (string direction)
# Output: reversed car position x, position y and direction
############################################################################
def test_reverse():
    
    #get user input
    input_vals = [2, 2, 'N']
    
    #run function
    vehicle_one = Vehicle(int(input_vals[0]), int(input_vals[1]), input_vals[2])
    vehicle_one.reverse(1.5)

    #test function
    assert vehicle_one.x == 2
    assert vehicle_one.y == 0.5
    assert vehicle_one.dir == 'N'





