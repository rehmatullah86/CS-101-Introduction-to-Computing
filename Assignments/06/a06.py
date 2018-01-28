## IMPORTS GO HERE

## END OF IMPORTS

### YOUR CODE FOR output_prime_factors() FUNCTION GOES HERE ###
def output_prime_factors(x):
    x = round(x)
    
    if x <= 1:
        print None
    
    
    d = 0
    while d < x:
        d = d + 1
        if x % d == 0:
            if  is_prime(d):
                print d
        
        
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


### YOUR CODE FOR get_nth_prime() FUNCTION GOES HERE ###
def get_nth_prime(x):
    
    count = 1
    a = 3
    while (count <= x) :
        if is_prime(a):
            count = count+1
            if count == x:
                return a
        a = round ( a + 2)
		
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


if __name__ == '__main__':
    output_prime_factors(23)
    print get_nth_prime(4)
