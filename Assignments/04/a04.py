## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(x):
    if x <= 100 and x >= 90:
        return 'A+'
    elif x >= 86:
        return 'A'
    elif x >= 82:
        return 'A-'
    elif x >= 78:
        return 'B+'
    elif x >= 74:
        return 'B'
    elif x >= 70:
        return 'B-'
    elif x >= 66:
        return 'C+'
    elif x >= 62:
        return 'C'
    elif x >= 58:
        return 'C-'
    elif x >= 54:
        return 'D+'
    elif x >= 50:
        return 'D'
    else:
        x >= 0
        return 'F'
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def grade(x):
	if x=="A+":
		return 4.00
	if x=="A":
		return 4.00
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
	    return 2.00
	if x=="C-":
		return 1.67
	if x=="D+":
	    return 1.33
	if x=="D":
		return 1.00
	if x=="F":
		return 0.00
		
		
		
		
def calculate_sgpa(value1,value2,value3):
	total_points = 0
	total_no_of_subjects = 0
	if value1 != 'nothing':
		total_no_of_subjects = total_no_of_subjects + 1
		total_points = total_points + grade(value1)
	if value2 != 'nothing':
		total_no_of_subjects = total_no_of_subjects + 1
		total_points = total_points + grade(value2)
	if value3 != 'nothing':
		total_no_of_subjects = total_no_of_subjects + 1
		total_points = total_points + grade(value3)
		
	if total_no_of_subjects == 0:
		return 
	else:
		sgpa = total_points/total_no_of_subjects
	return (sgpa)



def grade(x):
	if x=="A+":
		return 4.00
	if x=="A":
		return 4.00
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
	    return 2.00
	if x=="C-":
		return 1.67
	if x=="D+":
	    return 1.33
	if x=="D":
		return 1.00
	if x=="F":
		return 0.00
		
		
#### End OF MARKER




if __name__ == '__main__':
    print get_grade(50)
    print calculate_sgpa('A', 'B', 'nothing')
