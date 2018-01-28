## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR is_prime() FUNCTION GOES HERE ####
def is_prime(y):
    if y > 1:
        x = int(y)
        if x==y:
            if x == 1:
                return False
            if x == 0:
                return False
            if x == 2:
                return True
    
            if x >=2:
                if x>=2:
                    if x%2==0:
                        return False
                    for i in range(3,int(x**0.5)+1,2):
                        if x%i==0:
                            return False
            
            return True
        else:
            return False
    else:
        return False
    
    
#### End OF MARKER


#### YOUR CODE FOR output_factors() FUNCTION GOES HERE ####
def output_factors(x):
    d = 0
    while d < x:
        d = d + 1
        if x % d == 0:
            print d
#### End OF MARKER

#### YOUR CODE FOR get_largest_prime() FUNCTION GOES HERE ####
def get_largest_prime(z):
    
    if z >= 2:
    
        x=int(z)    
        if is_prime(x):
            return int(x)
        else:
            x = x-1
            return get_largest_prime(x)
    
    return None
#### End OF MARKER




if __name__ == '__main__':
    print is_prime(499)  # should return True

    print get_largest_prime(10)  # should return 7
    # print get_largest_prime(100000)  # bonus, try with 100k

    output_factors(10)  # should output -- 1 2 5 10 -- one on each line
