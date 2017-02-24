#!/usr/bin/python
# Author: Chanin Woods
# Built: python v.3.3
# Updated: 23 February 2017

############################################################################
# Class for vehicle object
# Parameters: x (float position), y (float position), dir (string direction)
# Functions:
# turn_left(self)
# turn_right(self)
# move(self)
# reverse(self, distance)
############################################################################
class Vehicle():

    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face
    
    ############################################################################
    # Function to turn vehicle toward left
    # Input: self object
    # Output: self object
    ############################################################################
    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]
    
    ############################################################################
    # Function to turn vehicle toward right
    # Input: self object
    # Output: self object
    ############################################################################
    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    ############################################################################
    # Function to move object one unit forward
    # Input: self object
    # Output: self object (position x or position y changes)
    ############################################################################
    def move(self):
        #initialize possible movements
        movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
        
        #move forward
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        #update position
        if new_x != self.x:
            self.x = new_x
        if new_y != self.y:
            self.y = new_y

    ############################################################################
    # Function to reverse the vehicle (moves backward, but doesn't flip around)
    # Input: distance (float distance to reverse)
    # Output: self object (position x or position y changes)
    ############################################################################
    def reverse(self, distance):
        
        #check inputs
        if not isinstance(distance, float) and not isinstance(distance, int):
            raise ValueError('distance variable must be a float')
        
        #reverse vehicle
        direction = self.dir
        if direction == 'N':
            self.y = self.y - distance
        elif direction == 'S':
            self.y = self.y + distance
        elif direction == 'W':
            self.x = self.x + distance
        elif direction == 'E':
            self.x = self.x - distance

        return{'x':self.x, 'y':self.y, 'dir':self.dir}

############################################################################
# Function to test code (command line input)
# Input: x (float position), y (float position), dir (string direction)
# Output: reversed car position x, position y and direction
############################################################################
def main():
    
    #get user input
    input_vals = [2, 2, 'N']
    
    #run function
    vehicle_one = Vehicle(int(input_vals[0]), int(input_vals[1]), input_vals[2])
    vehicle_rev = vehicle_one.reverse(1.5)

    #test function
    assert vehicle_rev['x'] == 2
    assert vehicle_rev['y'] == 0.5
    assert vehicle_rev['dir'] == 'N'



if (__name__=="__main__"):
    main()




