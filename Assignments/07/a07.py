## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ###
def calculate_sgpa(x):
    if x == None:
        return None
    if len(x) == 0:
        return 0
    b = len(x)
    totalpoints = 0
    if type(x) == str:
        return grade(x)
    for i in x:
        if grade(i) == None:
            return None
        totalpoints += (grade(i))
    
        
    return abs((totalpoints/b))
        
    
def grade(x):
    if x=="A+":
        return 4.0
    if x=="A":
        return 4.0
    if x=="A-":
        return 3.67
    if x=="B+":
        return 3.33
    if x=="B":
        return 3.00
    if x=="B-":
        return 2.67
    if x=="C+":
        return 2.33
    if x=="C":
        return 2.0
    if x=="C-":
        return 1.67
    if x=="D+":
        return 1.33
    if x=="D":
        return 1.0
    if x=="F":
        return 0.0
    else:
        return None
    
        
        
#### End OF MARKER

### YOUR CODE FOR calculate_sgpa_weighted() FUNCTION GOES HERE ###
def calculate_sgpa_weighted(x,y):
    if type(x) == str:
        return (grade(x) * y ) / y
    if len(x) != len(y):
        return None
    totalpoints = 0
    total_hours = 0
    
    for i in x:
        if grade(i) == None:
            return None
        for j in y:
            grade(i) * j
            totalpoints += grade(i) * j
            total_hours += j
            y.pop(0)
            break
    return totalpoints/total_hours




	
	

#### End OF MARKER


if __name__ == '__main__':
    print calculate_sgpa(['A+'])
    print calculate_sgpa_weighted(['A+'], [4])
