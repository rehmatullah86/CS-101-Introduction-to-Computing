## IMPORTS GO HERE

## END OF IMPORTS


### YOUR CODE FOR find_cumulative_marks() FUNCTION GOES HERE ###
def find_cumulative_marks(x):
    if x==[]:
        return []
    if x == None:
        return None
    y = []
    for i in x:
        a = list(i)
        c = 0
        b = []
        for j in a:
            if j == None:
                continue
            if type(j)== str:
                b.append(j)
                
            if type(j) == int or type(j) == float :
                c = c + j
        b.append(c)
                
                
                
        d = tuple(b)
        y.append(d)
    return y
                
#### End OF MARKER


### YOUR CODE FOR find_top_student() FUNCTION GOES HERE ###
def find_top_student(x):
    p = []
    
    a = find_cumulative_marks(x)
    
    q = list(a)
    c = 0
            
    
    for i in q:
        
        z = list(i)
        for j in z:
            if type(j)==int or type(j)==float:
                    
                if j > c:
                    c = j

    
    for i in q:
        for j in i:
            if type(j)==int or type(j)==float:
                if c ==j:
                    
                    s = list(i)
                    s.remove(j)
                    l = tuple(s)
                    
    for i in q:
        for j in i:
            if type(j)==int or type(j)==float:
                
                if j == c:
                    s = list(i)
                    s.remove(j)
                    z = tuple(s)
                    p.append(z)
    if len(p)==1:
        return l
    return p
                    
            

            

    


    

#### End OF MARKER





if __name__ == '__main__':
    results = [
        ('p101111', 'Ali Khayam', 64, 78.5, 89, 25, 99),
        ('p101112', 'Mudasser Farooq', 14, 28.5, 83, 76),
        ('p101113', 'Tamleek Ali', 87, None, 1.6)
    ]

    print find_cumulative_marks(results)
    # output: [('p101111', 'Ali Khayam', 355.5), ('p101112', 'Mudasser Farooq', 201.5), ('p101113', 'Tamleek Ali', 88.6)]

    print find_top_student(results)
    # output: ('p101111', 'Ali Khayam')
