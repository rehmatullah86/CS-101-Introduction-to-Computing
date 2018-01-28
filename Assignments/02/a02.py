## IMPORTS GO HERE
from math import pi
## END OF IMPORTS 


#### YOUR CODE FOR get_area GOES HERE ####
def get_area(r):
    a= pi * pow(r, 2)
    return a
#### End OF MARKER


#### YOUR CODE FOR output_parameter GOES HERE ####
def output_parameter(r):
    parameter = 2 * pi * (r)
    print "The parameter of the circle with radius", (r), "is", parameter,
#### End OF MARKER  





if __name__ == '__main__': 
    print get_area(2) 
    output_parameter(1.0) 

