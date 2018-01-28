## IMPORTS GO HERE
import os

## END OF IMPORTS



### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count(directory,name,y=False):
    filename = os.path.join(directory,name)
    with  open(filename,'r') as f:#handle
        if y == True:
            z =f.read().split('\n')
            while '' in z:
                z.remove('')
            
            return len(z)
        if y != True:    
            c = 1
            for line in f:
                c += 1
            
            return c
    

    

    
    
    
#### End OF MARKER



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(directory,name,y=False):
    filename = os.path.join(directory,name)
    with  open(filename,'r') as f:#handle
        if y == True:
            v = f.read().split('\n')
            q = 0
            for line in v:
                for chars in line:
                    if chars == ' ' :
                        continue
                    q=q+1
            return q 
            
            return len(z)
        if y != True: 
            c = 0
            for line in f:
                for char in line:
                    c=c+1
            return c
            
    

    
    

    
#### End OF MARKER


if __name__ == '__main__':
    print line_count('.', 'essay.txt')
    print line_count('.', 'essay.txt', True)

    print character_count('.', 'essay.txt')
    print character_count('.', 'essay.txt', True)

    move_lines('essay.txt', 'out.txt', 3)

    pass
