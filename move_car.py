# General:
# 1) add comments
# 2) add unit tests instead of printing tests
# 3) state what python version is being used
# 4) include author names

# Line Item:
# Missing comments line 15
# Missing function line 21
# Missing input tests line 30
# Inefficient eval line 57
# Unused code line 65
# Repeated code line 70
# Syntax problem line 79

# Missing comments
# describe what each of these parameters is encoding
directions = ['N','E','S','W']
movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}
commands = {'L': 'turn_left', 'R': 'turn_right', 'M': 'move'}

# Missing function
# What is the raw_input() function? Should it be called from another class or included here?
# If it is from an older version of python, specify what version or allow for both
GRID_MAX_X, GRID_MAX_Y = map(int, raw_input().split())

first_vehicle_x = None
first_vehicle_y = None

class Vehicle():
    # Missing input tests
    # check to see if input is the correct type (or convert it to the correct type)
    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.dir = face

    def turn_left(self):
        self.dir = directions[(directions.index(self.dir)-1)%len(directions)]

    def turn_right(self):
        self.dir = directions[(directions.index(self.dir)+1)%len(directions)]

    def move(self):
        new_x = self.x + movement[self.dir][0]
        new_y = self.y + movement[self.dir][1]

        if new_x != first_vehicle_x or new_y != first_vehicle_y:
            if new_x in xrange(GRID_MAX_X+1):
                self.x = new_x
            if new_y in xrange(GRID_MAX_Y+1):
                self.y = new_y


vehicle_one_pos = raw_input().split()
vehicle_one_commands = raw_input()

# Inefficient eval
# remove the eval and replace with a faster, easier to debug solution
# consider creating an empty array and filling
vehicle_one = Vehicle(int(vehicle_one_pos[0]), int(vehicle_one_pos[1]), vehicle_one_pos[2])
for command in vehicle_one_commands:
    eval("vehicle_one.{0}()".format(commands[command]))

# Unused code
# Remove these lines, if unsued
first_vehicle_x = vehicle_one.x
first_vehicle_y = vehicle_one.y

# Repeated code
# create a function that runs lines 55-63 and use that for both vehicle 1 and 2
vehicle_two_pos = raw_input().split()
vehicle_two_commands = raw_input()

vehicle_two = Vehicle(int(vehicle_two_pos[0]), int(vehicle_two_pos[1]), vehicle_two_ps[2])
for command in vehicle_two_commands:
    eval("vehicle_two.{0}()".format(commands[command]))

# Syntax problem
# print statement must have parentheses in python v3 and higher
print vehicle_one.x, vehicle_one.y, vehicle_one.dir
print vehicle_two.x, vehicle_two.y, vehicle_two.dir






